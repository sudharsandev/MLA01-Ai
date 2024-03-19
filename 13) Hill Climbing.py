import random

def hill_climbing(problem, max_iterations=1000):
    current_solution = problem.initial_solution()
    for _ in range(max_iterations):
        neighbors = problem.get_neighbors(current_solution)
        next_solution = max(neighbors, key=problem.heuristic)
        if problem.heuristic(next_solution) <= problem.heuristic(current_solution):
            break
        current_solution = next_solution
    return current_solution

# Example problem
class ExampleProblem:
    def initial_solution(self):
        return [random.randint(0, 100) for _ in range(5)]

    def get_neighbors(self, solution):
        return [[max(0, min(100, x + random.randint(-10, 10))) for x in solution] for _ in range(len(solution))]

    def heuristic(self, solution):
        return sum(solution)

problem = ExampleProblem()
solution = hill_climbing(problem)
print("Optimal solution:", solution)
print("Optimal value:", problem.heuristic(solution))
