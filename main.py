import matplotlib.pyplot
import networkx

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

# Plot the DAG
pos = networkx.spring_layout(dag)
networkx.draw(
    dag,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_size=10,
    font_weight="bold",
    arrowsize=20,
)

# Show the plot
matplotlib.pyplot.show()
