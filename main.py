import networkx

# Create a Directed Acyclic Graph (DAG)
dag = networkx.DiGraph()

# Define nodes and edges
nodes = ["Task A", "Task B", "Task C", "Task D", "Task E", "Task F"]
edges = [
    ("Task A", "Task B"),
    ("Task A", "Task C"),
    ("Task B", "Task D"),
    ("Task C", "Task D"),
    ("Task E", "Task F"),
    ("Task C", "Task E"),
]

# Add nodes and edges to the DAG
dag.add_nodes_from(nodes)
dag.add_edges_from(edges)

# Display DAG dependencies in a text-based format
for node in nodes:
    dependencies = list(dag.predecessors(node))
    if dependencies:
        print(f"{node} depends on: {', '.join(dependencies)}")
    else:
        print(f"{node} has no dependencies")
