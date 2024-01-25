import argparse
import io

import networkx


class PrintStrategy:
    def print_dependencies(self):
        raise NotImplementedError("Subclasses must implement print_dependencies method")


class ConsolePrint(PrintStrategy):
    def print_dependencies(self, nodes_with_dependencies, output_stream):
        total_nodes = len(nodes_with_dependencies)

        for index, (node, dependencies) in enumerate(nodes_with_dependencies, start=1):
            if dependencies:
                output_stream.write(f"{node} depends on: {', '.join(dependencies)}")
            else:
                output_stream.write(f"{node} has no dependencies")

            if index < total_nodes:
                output_stream.write("\n")


class ConsolePrintAsciiArt(PrintStrategy):
    def print_dependencies(self, nodes_with_dependencies, output_stream):
        total_nodes = len(nodes_with_dependencies)

        for index, (node, dependencies) in enumerate(nodes_with_dependencies, start=1):
            output_stream.write(f"{node}")

            if index < total_nodes:
                output_stream.write("\n")

            for depth, dep in enumerate(dependencies, start=1):
                output_stream.write(f"{'  ' * depth}└── {dep}")

                if index < total_nodes:
                    output_stream.write("\n")


def main(print_strategy: PrintStrategy, output_stream: io.StringIO):
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

    if print_strategy:
        # Display DAG dependencies based on the injected strategy
        print_strategy.print_dependencies(nodes_with_dependencies, output_stream)


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
        "--print-asciiart",
        action="store_true",
        default=False,
        help="Print dependencies using tabs to show nesting.",
    )
    args = parser.parse_args()

    output_stream = io.StringIO()

    print_strategy = None

    # Instantiate the appropriate print strategy
    if args.print_console:
        print_strategy = ConsolePrint()
    elif args.print_asciiart:
        print_strategy = ConsolePrintAsciiArt()

    # Call the main function with the chosen strategy and output destination
    main(print_strategy=print_strategy, output_stream=output_stream)

    if output_stream.getvalue():
        print(output_stream.getvalue())
