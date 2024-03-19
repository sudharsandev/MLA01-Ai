import itertools

def tsp(cities, distances, start):
    shortest_distance = float('inf')
    shortest_path = None

    for path in itertools.permutations(cities):
        if path[0] != start:
            continue
        distance = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
        distance += distances[path[-1]][path[0]]

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance

# Example usage:
cities = ['A', 'B', 'C']
distances = {
    'A': {'A': 0, 'B': 10, 'C': 15},
    'B': {'A': 10, 'B': 0, 'C': 20},
    'C': {'A': 15, 'B': 20, 'C': 0}
}
start_city = 'A'

shortest_path, shortest_distance = tsp(cities, distances, start_city)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)
