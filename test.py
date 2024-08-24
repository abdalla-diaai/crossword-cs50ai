from crossword import *
from generate import *

overlap = {(Variable(2, 1, 'down', 5), Variable(1, 12, 'down', 7)): None, 
           (Variable(2, 1, 'down', 5), Variable(4, 4, 'across', 5)): None, 
           (Variable(2, 1, 'down', 5), Variable(2, 1, 'across', 12)): (0, 0), 
           (Variable(2, 1, 'down', 5), Variable(1, 7, 'down', 7)): None, 
           (Variable(2, 1, 'down', 5), Variable(6, 5, 'across', 6)): None, 
           (Variable(1, 12, 'down', 7), Variable(2, 1, 'down', 5)): None, 
           (Variable(1, 12, 'down', 7), Variable(4, 4, 'across', 5)): None, 
           (Variable(1, 12, 'down', 7), Variable(2, 1, 'across', 12)): (1, 11), 
           (Variable(1, 12, 'down', 7), Variable(1, 7, 'down', 7)): None, 
           (Variable(1, 12, 'down', 7), Variable(6, 5, 'across', 6)): None, 
           (Variable(4, 4, 'across', 5), Variable(2, 1, 'down', 5)): None, 
           (Variable(4, 4, 'across', 5), Variable(1, 12, 'down', 7)): None, 
           (Variable(4, 4, 'across', 5), Variable(2, 1, 'across', 12)): None, 
           (Variable(4, 4, 'across', 5), Variable(1, 7, 'down', 7)): (3, 3), 
           (Variable(4, 4, 'across', 5), Variable(6, 5, 'across', 6)): None, 
           (Variable(2, 1, 'across', 12), Variable(2, 1, 'down', 5)): (0, 0), 
           (Variable(2, 1, 'across', 12), Variable(1, 12, 'down', 7)): (11, 1), 
           (Variable(2, 1, 'across', 12), Variable(4, 4, 'across', 5)): None, 
           (Variable(2, 1, 'across', 12), Variable(1, 7, 'down', 7)): (6, 1), 
           (Variable(2, 1, 'across', 12), Variable(6, 5, 'across', 6)): None, 
           (Variable(1, 7, 'down', 7), Variable(2, 1, 'down', 5)): None, 
           (Variable(1, 7, 'down', 7), Variable(1, 12, 'down', 7)): None, 
           (Variable(1, 7, 'down', 7), Variable(4, 4, 'across', 5)): (3, 3), 
           (Variable(1, 7, 'down', 7), Variable(2, 1, 'across', 12)): (1, 6), 
           (Variable(1, 7, 'down', 7), Variable(6, 5, 'across', 6)): (5, 2), 
           (Variable(6, 5, 'across', 6), Variable(2, 1, 'down', 5)): None, 
           (Variable(6, 5, 'across', 6), Variable(1, 12, 'down', 7)): None, 
           (Variable(6, 5, 'across', 6), Variable(4, 4, 'across', 5)): None, 
           (Variable(6, 5, 'across', 6), Variable(2, 1, 'across', 12)): None, 
           (Variable(6, 5, 'across', 6), Variable(1, 7, 'down', 7)): (2, 5)}




arcs = [(Variable(2, 1, 'across', 12), Variable(2, 1, 'down', 5)), (Variable(2, 1, 'across', 12), Variable(1, 12, 'down', 7)), (Variable(2, 1, 'across', 12), Variable(1, 7, 'down', 7)), (Variable(2, 1, 'across', 12), Variable(4, 4, 'across', 5)), (Variable(6, 5, 'across', 6), Variable(2, 1, 'across', 12)), (Variable(6, 5, 'across', 6), Variable(2, 1, 'down', 5)), (Variable(6, 5, 'across', 6), Variable(1, 12, 'down', 7)), (Variable(6, 5, 'across', 6), Variable(1, 7, 'down', 7)), (Variable(6, 5, 'across', 6), Variable(4, 4, 'across', 5)), (Variable(2, 1, 'down', 5), Variable(2, 1, 'across', 12)), (Variable(2, 1, 'down', 5), Variable(6, 5, 'across', 6)), (Variable(2, 1, 'down', 5), Variable(1, 12, 'down', 7)), (Variable(2, 1, 'down', 5), Variable(1, 7, 'down', 7)), (Variable(2, 1, 'down', 5), Variable(4, 4, 'across', 5)), (Variable(1, 12, 'down', 7), Variable(2, 1, 'across', 12)), (Variable(1, 12, 'down', 7), Variable(6, 5, 'across', 6)), (Variable(1, 12, 'down', 7), Variable(2, 1, 'down', 5)), (Variable(1, 12, 'down', 7), Variable(1, 7, 'down', 7)), (Variable(1, 12, 'down', 7), Variable(4, 4, 'across', 5)), (Variable(1, 7, 'down', 7), Variable(2, 1, 'across', 12)), (Variable(1, 7, 'down', 7), Variable(6, 5, 'across', 6)), (Variable(1, 7, 'down', 7), Variable(2, 1, 'down', 5)), (Variable(1, 7, 'down', 7), Variable(1, 12, 'down', 7)), (Variable(1, 7, 'down', 7), Variable(4, 4, 'across', 5)), (Variable(4, 4, 'across', 5), Variable(2, 1, 'across', 12)), (Variable(4, 4, 'across', 5), Variable(6, 5, 'across', 6)), (Variable(4, 4, 'across', 5), Variable(2, 1, 'down', 5)), (Variable(4, 4, 'across', 5), Variable(1, 12, 'down', 7)), (Variable(4, 4, 'across', 5), Variable(1, 7, 'down', 7))]

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
    creator.enforce_node_consistency()
    my_dict = {'HELLO': 0, 'COINS': 3}
    my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    print(list(my_dict.keys()))

if __name__ == "__main__":
    main()
