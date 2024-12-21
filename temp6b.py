def find_loop_positions(grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    current_direction = 0
    row, col = 0, 0  # Starting position

    loop_positions = []
    visited = set()

    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        visited.add((row, col, current_direction))

        # Check if the current position is a potential loop point
        if grid[row][col] == '#':
            for i in range(1, 3):
                new_direction = (current_direction + i) % 4
                dr, dc = directions[new_direction]
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '#':
                    # Check if turning back to the original direction creates a loop
                    original_direction = (new_direction + 2) % 4
                    original_dr, original_dc = directions[original_direction]
                    original_row, original_col = new_row + original_dr, new_col + original_dc

                    if 0 <= original_row < len(grid) and 0 <= original_col < len(grid[0]) and (
                    original_row, original_col, original_direction) in visited:
                        loop_positions.append((new_row, new_col))

        # Move to the next position
        dr, dc = directions[current_direction]
        row += dr
        col += dc

    return loop_positions


# Example usage:
grid = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

loop_positions = find_loop_positions(grid)
print(loop_positions)
