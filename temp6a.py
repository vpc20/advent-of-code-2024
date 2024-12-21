def solve_part_1(grid, start_row, start_col):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    curr_dir = 0
    dr, dc = dirs[curr_dir]
    row, col = start_row, start_col
    visited = {(row, col)}

    while 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
        # Turn right before checking the obstruction
        if grid[row + dr][col + dc] == '#':
            curr_dir = (curr_dir + 1) % 4
            dr, dc = dirs[curr_dir]
        row += dr
        col += dc

        if (row, col) not in visited:
            visited.add((row, col))

    return len(visited)


# Assuming you have a way to parse the grid and starting position from the input
filename = 'aoc6data1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

grid = [[c for c in s] for s in texts]
nrows = len(grid)
ncols = len(grid[0])
for i in range(nrows):
    for j in range(ncols):
        if grid[i][j] == '^':
            start_row = i
            start_col = j

result = solve_part_1(grid, start_row, start_col)
print(f"Part 1: {result}")
