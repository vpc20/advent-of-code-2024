import copy


def find_loop_positions(grid):
    rows, cols = len(grid), len(grid[0])
    loop_positions = []

    for row in range(rows):
        print(row)
        for col in range(cols):
            if grid[row][col] == '.':
                # Create a copy of the grid with the current '.' replaced with '#'
                new_grid = [list(row) for row in grid]
                new_grid[row][col] = '#'

                # Check for loop in the modified grid
                if check_for_loop(new_grid):
                    loop_positions.append((row, col))

    return len(loop_positions)


def check_for_loop(grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    rows, cols = len(grid), len(grid[0])

    # Find the initial position and direction
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '^':
                direction_index = 3  # Up
                break
        else:
            continue
        break

    visited = set()
    visited.add((row, col, direction_index))

    while True:
        d_row, d_col = directions[direction_index]
        new_row, new_col = row + d_row, col + d_col

        # Check if the new position is within the grid bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '#':  # Obstacle ahead
                direction_index = (direction_index + 1) % 4
            else:
                row, col = new_row, new_col
                new_state = (row, col, direction_index)
                if new_state in visited:
                    return True
                visited.add(new_state)
        else:
            # If the guard moves out of the grid, it's not a loop
            return False


filename = 'aoc6data1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

grid = [[c for c in s] for s in texts]
nrows = len(grid)
ncols = len(grid[0])
grid_bak = copy.deepcopy(grid)

for e in grid:
    print(e)

print(find_loop_positions(grid))
