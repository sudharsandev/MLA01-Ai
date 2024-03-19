class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        colors = {}
        for node in self.graph:
            neighbor_colors = set()
            for neighbor in self.graph[node]:
                if neighbor in colors:
                    neighbor_colors.add(colors[neighbor])
            for color in range(len(self.graph)):
                if color not in neighbor_colors:
                    colors[node] = color
                    break
        return colors

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

colors = g.greedy_coloring()
print("Node colors:", colors)
