class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.moves = []

    def clean_all(self):
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == 'dirty':
                    self.moves.append((r, c))

    def move(self, dr, dc):
        r, c = self.moves[-1]
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < len(self.grid) and 0 <= new_c < len(self.grid[0]):
            self.moves.append((new_r, new_c))
            return True
        return False

    def move_left(self):
        return self.move(0, -1)

    def move_right(self):
        return self.move(0, 1)

    def move_up(self):
        return self.move(-1, 0)

    def move_down(self):
        return self.move(1, 0)

    def print_moves(self):
        for r, c in self.moves:
            print(f"Clean cell at ({r}, {c})")

# Example usage:
grid = [
    ['dirty', 'clean', 'dirty'],
    ['clean', 'dirty', 'clean'],
    ['dirty', 'clean', 'dirty']
]
vacuum = VacuumCleaner(grid)
vacuum.clean_all()
vacuum.move_down()
vacuum.move_right()
vacuum.move_down()
vacuum.move_left()
vacuum.print_moves()
