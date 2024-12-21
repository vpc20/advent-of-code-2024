def parse_input(input_data):
    """
    Parse the input data into a 2D grid.
    """
    return [list(line.strip()) for line in input_data.splitlines()]


def count_visible_in_direction(grid, i, j, di, dj):
    """
    Count how many '.' cells are visible in a given direction (di, dj) from position (i, j).
    This counts until we hit a non-'.' cell or the grid boundary.
    """
    height = len(grid)
    width = len(grid[0])
    count = 0
    x, y = i + di, j + dj

    # Keep counting until we hit the edge of the grid or a non-'0' or 'A' symbol.
    while 0 <= x < height and 0 <= y < width and grid[x][y] == '.':
        count += 1
        x += di
        y += dj

    return count


def calculate_scenic_score(grid):
    """
    Calculate the maximum scenic score for any '0' or 'A' symbol in the grid.
    The score is the product of the visible count in all four directions.
    """
    max_scenic_score = 0
    height = len(grid)
    width = len(grid[0])

    # Direction vectors for up, down, left, right (dy, dx)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    # Traverse the grid
    for i in range(height):
        for j in range(width):
            if grid[i][j] in ('0', 'A'):  # Only calculate for '0' or 'A'
                visibility_score = 1  # Start with 1 (itself)
                for di, dj in directions:
                    visibility_score *= (count_visible_in_direction(grid, i, j, di, dj) + 1)
                max_scenic_score = max(max_scenic_score, visibility_score)

    return max_scenic_score


def solve_part_2(input_data):
    """
    The main function to solve Part 2 of the problem based on visibility.
    """
    grid = parse_input(input_data)
    return calculate_scenic_score(grid)


# Example usage:
input_data = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""  # Example input
result = solve_part_2(input_data)
print(f"Maximum scenic score: {result}")
