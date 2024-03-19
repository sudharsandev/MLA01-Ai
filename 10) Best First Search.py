import heapq

def best_first_search(graph, start, goal):
    visited = set()
    queue = [(0, start)]

    while queue:
        _, node = heapq.heappop(queue)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            if node == goal:
                return
            for neighbor, cost in sorted(graph[node], key=lambda x: x[1]):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost, neighbor))

# Example usage:
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('D', 6), ('E', 7)],
    'C': [('A', 5), ('F', 8)],
    'D': [('B', 6)],
    'E': [('B', 7), ('F', 9)],
    'F': [('C', 8), ('E', 9)]
}
start_node = 'A'
goal_node = 'F'

print("Best-First Search:")
best_first_search(graph, start_node, goal_node)
