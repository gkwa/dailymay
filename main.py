import argparse

import networkx


class SimplePrint:
    @staticmethod
    def print_dependencies(nodes_with_dependencies):
        for node, dependencies in nodes_with_dependencies:
            if dependencies:
                print(f"{node} depends on: {', '.join(dependencies)}")
            else:
                print(f"{node} has no dependencies")


def main():
    parser = argparse.ArgumentParser(
        description="Create and display a Directed Acyclic Graph (DAG)."
    )
    parser.add_argument(
        "--print-simple",
        action="store_true",
        default=True,
        help="Use SimplePrint strategy for printing (default: True).",
    )
    args = parser.parse_args()

    # Create a Directed Acyclic Graph (DAG)
    dag = networkx.DiGraph()

    # Define nodes and edges
    nodes = ["Task A", "Task B", "Task C", "Task D"]
    edges = [
        ("Task A", "Task B"),
        ("Task A", "Task C"),
        ("Task B", "Task D"),
        ("Task C", "Task D"),
    ]

    # Add nodes and edges to the DAG
    dag.add_nodes_from(nodes)
    dag.add_edges_from(edges)

    # Get nodes and their dependencies
    nodes_with_dependencies = [(node, list(dag.predecessors(node))) for node in nodes]

    # Display DAG dependencies based on the chosen strategy
    if args.print_simple:
        SimplePrint.print_dependencies(nodes_with_dependencies)
    else:
        print("Please specify a valid printing strategy.")


if __name__ == "__main__":
    main()
