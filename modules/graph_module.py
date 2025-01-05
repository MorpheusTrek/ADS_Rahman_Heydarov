import pickle
import networkx as nx
import matplotlib.pyplot as plt

import pickle
import networkx as nx
import matplotlib.pyplot as plt

class GraphModule:
    def __init__(self):
        self.file_path = "graph_data.gpickle"  # File path for saving and loading the graph
        self.graph = self.load_graph()  # Load or initialize the graph

    def save_graph(self):
        # Save the current state of the graph to a file.
        # This ensures that changes to the graph are persisted for future use.
        with open(self.file_path, "wb") as f:
            pickle.dump(self.graph, f, pickle.HIGHEST_PROTOCOL)

    def load_graph(self):
        # Load the graph from a file if it exists; otherwise, create an empty directed graph.
        try:
            with open(self.file_path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            # Return a new empty directed graph if no saved graph exists
            return nx.DiGraph()

    def add_task(self, tasks):
        # Add tasks with dependencies to the graph.
        # Each pair of consecutive tasks in the list creates a directed edge in the graph.
        if len(tasks) < 2:
            print("Error: Provide at least two tasks for a dependency.")
            return
        for i in range(len(tasks) - 1):
            self.graph.add_edge(tasks[i], tasks[i + 1])  # Add a directed edge for each dependency
        self.save_graph()  # Save the updated graph
        print("Tasks added successfully.")

    def display(self):
        # Display the graph and perform cycle detection or topological sorting.
        try:
            # Attempt to find a cycle in the graph
            cycle = list(nx.find_cycle(self.graph, orientation="original"))
            print(f"Cycle detected: {cycle}")
        except nx.NetworkXNoCycle:
            # If no cycle is found, perform topological sorting and display the graph
            print("No cycle detected. Topological Order:")
            topo_order = list(nx.topological_sort(self.graph))
            print(topo_order)  # Print the topological order of tasks
            # Visualize the graph
            nx.draw(self.graph, with_labels=True, node_color="lightblue", font_weight="bold")
            plt.show()

    def topological_sort(self):
        # Compute and print the topological order of tasks in the graph.
        # If the graph contains a cycle, inform the user.
        try:
            # Perform topological sorting
            topo_order = list(nx.topological_sort(self.graph))
            print("Topological Order of Task Completion:")
            print(" -> ".join(topo_order))  # Display the topological order in a readable format
            return topo_order
        except nx.NetworkXUnfeasible:
            # Inform the user if topological sorting is not possible due to a cycle
            print("Topological sorting is not possible; the graph contains a cycle.")
            return None