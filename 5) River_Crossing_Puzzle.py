from collections import deque

def is_valid(state):
    for shore in state:
        if shore[1] > shore[0] > 0 or shore[1] < shore[0] < 3:
            return False
    return True

def cross_river(start_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, moves = queue.popleft()
        if current_state == ((0, 0), (3, 3)):
            return moves
        if current_state not in visited:
            visited.add(current_state)
            for move in get_valid_moves(current_state):
                queue.append((move[0], moves + [move[1]]))
    return None

def get_valid_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[0][i] and state[0][i] >= state[1][j] or state[0][i] == 0:
                new_state = (
                    tuple(state[0][k] - (1 if k == i else 0) for k in range(3)),
                    tuple(state[1][k] + (1 if k == j else 0) for k in range(3))
                )
                if is_valid(new_state):
                    moves.append((new_state, (i, j)))
    return moves

start_state = ((3, 3), (0, 0))
solution = cross_river(start_state)
if solution:
    print("Solution found in", len(solution), "moves:")
    for move in solution:
        print(move)
else:
    print("No solution found.")
