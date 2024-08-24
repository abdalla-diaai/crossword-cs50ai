import sys

from crossword import *


class CrosswordCreator:

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy() for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size, self.crossword.height * cell_size),
            "black",
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border, i * cell_size + cell_border),
                    (
                        (j + 1) * cell_size - cell_border,
                        (i + 1) * cell_size - cell_border,
                    ),
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (
                                rect[0][0] + ((interior_size - w) / 2),
                                rect[0][1] + ((interior_size - h) / 2) - 10,
                            ),
                            letters[i][j],
                            fill="black",
                            font=font,
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # remove words that is not unary consistent
        for domain, words in self.domains.items():
            for word in words.copy():
                if len(word) != domain.length:
                    self.domains[domain].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # gather all overlaps
        overlaps = self.crossword.overlaps
        # get overlap between x and y
        overlap = overlaps[x, y]
        # if overlap is None, return None
        if overlap is None:
            return False
        i, j = overlap
        revised = False
        new_domain_x = set()
        for value_x in self.domains[x]:
            # add only words in x domain that are binary consistent with y
            if any(value_x[i] == value_y[j] for value_y in self.domains[y]):
                new_domain_x.add(value_x)
            else:
                # if a word is not binary consistent with y change revised to true
                revised = True
        # assign words that are binary consistent with y to x
        self.domains[x] = new_domain_x
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # if arcs is None, use all arcs
        if arcs is None:
            arcs = list(self.crossword.overlaps)
        else:
            # if arcs is provided use it
            arcs = list(arcs)
        while len(arcs) > 0:
            arc = arcs.pop()
            x = arc[0]
            y = arc[1]
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x) - {y}:
                    arcs.append((z, x))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # check if all variables in assignment
        if all(key in assignment for key in self.crossword.variables):
            # check if all variables have a value
            if all(assignment[key] for key in assignment):
                return True
        return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        overlaps = self.crossword.overlaps
        for k1, v1 in assignment.items():
            # Check that all words are of the correct length and distinct (unary constraints)
            if len(v1) != k1.length:
                return False
            if list(assignment.values()).count(v1) > 1:
                return False
            # check for binary constraints
            for k2, v2 in assignment.items():
                if k1 == k2:
                    continue
                if overlaps[k1, k2] is None or (k1, k2) not in overlaps:
                    continue
                i, j = self.crossword.overlaps[k1, k2]
                if v1[i] != v2[j]:
                    return False
        return True

    def sort_dict_by_values(self, d):
        """
        Helper function.

        Return a list of dictionary (d) keys sorted by dictionary (d) values in ascending order
        """
        return sorted(d, key=d.get)

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # get values for this var
        domain_values = self.domains[var]
        # initialise dictionary with all domain values and count 0
        values_dict = {key: 0 for key in domain_values}
        # get neighbors of this var
        neighbors = self.crossword.neighbors(var)
        # get all overlaps
        overlaps = self.crossword.overlaps
        # count how many values for neighbor are being excluded for each neighbor of this var
        for neighbor in neighbors:
            count = 0
            # consider unassigned neighbors only
            if neighbor not in assignment.keys():
                # check for overlap and it is not None
                if (var, neighbor) in overlaps:
                    if overlaps[var, neighbor] is None:
                        count += 0
                    i, j = overlaps[var, neighbor]
                    for val1 in domain_values:
                        for val2 in self.domains[neighbor]:
                            # check for binary constraint
                            if val1[i] != val2[j]:
                                count += 1
                        values_dict[val1] = count
        # order values in ascending order
        return self.sort_dict_by_values(values_dict)

    def get_min_value_keys(self, d):
        """
        Helper function.
        Return a list of keys with minimum value in dictionary including ties.
        """
        # Find the maximum value in the dictionary
        min_value = min(d.values())
        # Return the keys that have the maximum value
        return [key for key, value in d.items() if value == min_value]

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # dict to hold values of unassinged variables
        unassigned_vars = {}
        # add number of domains to each variable
        for var in self.crossword.variables:
            if var not in assignment:
                unassigned_vars[var] = len(self.domains[var])
        min_var = self.get_min_value_keys(unassigned_vars)
        # if only one var returned, return var with min number of domains
        if len(min_var) == 1:
            return min_var[0]
        else:
            # return var with max neighbors or any in case of tie
            maximum_neighbors = len(self.crossword.neighbors(min_var[0]))
            max_var = min_var[0]
            for item in min_var:
                if len(self.crossword.neighbors(item)) > maximum_neighbors:
                    maximum_neighbors = len(self.crossword.neighbors(item))
                    max_var = item
            return max_var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.
        `assignment` is a mapping from variables (keys) to words (values).
        If no assignment is possible, return None.
        """
        # return complete assignment if it exists.
        if self.assignment_complete(assignment):
            return assignment
        # get one of unassinged variables
        var = self.select_unassigned_variable(assignment)
        # order values in variable domain
        var_values = self.order_domain_values(var, assignment)
        # iterate through values and check assignment for consistency
        for val in var_values:
            new_assignment = assignment.copy()
            # add new value to assignment
            new_assignment[var] = val
            # check for consistency
            if self.consistent(new_assignment):
                # recursively call backtrack function
                result = self.backtrack(new_assignment)
                return result
            else:
                new_assignment.pop(var)
        # if no result return None
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
