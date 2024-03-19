import heapq

def astar(maze, start, end):
    open_list = []
    heapq.heappush(open_list, (0, start, None))
    visited = set()
    while open_list:
        _, current, parent = heapq.heappop(open_list)
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent
            return path[::-1]
        if current in visited:
            continue
        visited.add(current)
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = current[0] + i, current[1] + j
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0:
                heapq.heappush(open_list, (abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1]), neighbor, current))

# Example usage
maze = [
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 5)

path = astar(maze, start, end)
print("Path found:", path)
