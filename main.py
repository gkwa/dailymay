import argparse

import networkx


class PrintStrategy:
    def print_dependencies(self, nodes_with_dependencies):
        raise NotImplementedError("Subclasses must implement print_dependencies method")


class ConsolePrint(PrintStrategy):
    def print_dependencies(self, nodes_with_dependencies):
        for node, dependencies in nodes_with_dependencies:
            if dependencies:
                print(f"{node} depends on: {', '.join(dependencies)}")
            else:
                print(f"{node} has no dependencies")


class ConsolePrint2(PrintStrategy):
    def print_dependencies(self, nodes_with_dependencies):
        for node, dependencies in nodes_with_dependencies:
            print(f"{node}")
            for depth, dep in enumerate(dependencies, start=1):
                print(f"{'  ' * depth}└── {dep}")


def main(print_strategy: PrintStrategy):
    # Create a Directed Acyclic Graph (DAG)
    dag = networkx.DiGraph()

    # Define nodes and edges
    nodes = [
        "Task A",
        "Task B",
        "Task C",
        "Task D",
        "Task E",
        "Task F",
    ]
    edges = [
        ("Task A", "Task B"),
        ("Task A", "Task C"),
        ("Task B", "Task D"),
        ("Task C", "Task D"),
        ("Task F", "Task E"),
        ("Task A", "Task E"),
    ]

    # Add nodes and edges to the DAG
    dag.add_nodes_from(nodes)
    dag.add_edges_from(edges)

    # Get nodes and their dependencies
    nodes_with_dependencies = [(node, list(dag.predecessors(node))) for node in nodes]

    # Display DAG dependencies based on the injected strategy
    print_strategy.print_dependencies(nodes_with_dependencies)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create and display a Directed Acyclic Graph (DAG)."
    )
    parser.add_argument(
        "--print-console",
        action="store_true",
        default=False,
        help="Use ConsolePrint strategy for printing.",
    )
    parser.add_argument(
        "--print-console2",
        action="store_true",
        default=False,
        help="Print dependencies using tabs to show nesting.",
    )
    args = parser.parse_args()

    # Instantiate the appropriate print strategy
    if args.print_console:
        strategy = ConsolePrint()
    elif args.print_console2:
        strategy = ConsolePrint2()
    else:
        parser.print_help()
        print("Please specify a valid printing strategy.")
        exit(1)

    # Call the main function with the chosen strategy
    main(print_strategy=strategy)
