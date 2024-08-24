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

assign = { Variable(2, 1, 'down', 5): {'LOGIC', 'TRUTH', 'GRAPH', 'PRUNE', 'START', 'INFER', 'BAYES', 'ALPHA', 'DEPTH', 'FALSE'}, Variable(2, 1, 'across', 12): {'INTELLIGENCE', 'DISTRIBUTION', 'OPTIMIZATION', 'SATISFACTION'}, Variable(1, 7, 'down', 7): {'NETWORK', 'RESOLVE', 'INITIAL', 'BREADTH', 'MINIMAX'}}
# Variable(6, 5, 'across', 6): {'SEARCH', 'REASON', 'MARKOV', 'CREATE', 'NEURAL'}
# Variable(4, 4, 'across', 5): {'LOGIC', 'TRUTH', 'GRAPH', 'PRUNE', 'START', 'INFER', 'BAYES', 'ALPHA', 'DEPTH', 'FALSE'},
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

if __name__ == "__main__":
    main()
