import argparse
import ast
from alhazen import Alhazen
from alhazen_formalizations.calculator import prop
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Alhazen CLI')
    parser.add_argument('--input', '-i', metavar='INPUT_FILE', type=str, required=True,
                        help='Path to the input file containing initial inputs')
    parser.add_argument('--grammar', '-g', metavar='GRAMMAR_FILE', required=True,
                        help='Path to the grammar file,'
                             'The grammar content should be a string representing a dictionary')

    args = parser.parse_args()

    # Read initial inputs from the input file
    with open(args.input, 'r') as f:
        content = f.read()
        initial_inputs = ast.literal_eval(content)

    # Read grammar from the grammar file
    with open(args.grammar, 'r') as file:
        grammar = ast.literal_eval(file.read())

    # Create an instance of Alhazen
    alhazen = Alhazen(
        initial_inputs=initial_inputs,
        grammar=grammar,
        evaluation_function=prop
    )

    # Run Alhazen
    models = alhazen.run()

    decision_trees = [tree for tree in models if isinstance(tree, DecisionTreeClassifier)]
    for i, tree in enumerate(decision_trees):
        plt.figure(figsize=(10, 8))
        plot_tree(tree, filled=True, rounded=True, class_names=["NO_BUG", "BUG"])
        plt.title(f"Decision Tree {i + 1}")
        plt.show()


if __name__ == "__main__":
    main()
