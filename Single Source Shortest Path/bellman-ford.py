class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, source):
        # Initialize distances from source to all other vertices as infinity
        distances = [float("inf")] * self.V
        distances[source] = 0

        # Relaxation step (V - 1) times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distances[u] != float("inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.graph:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                print("Graph contains a negative-weight cycle")
                return

        # Print the distances
        self.print_distances(distances)

    def print_distances(self, distances):
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{distances[i]}")


# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)
g.bellman_ford(0)
