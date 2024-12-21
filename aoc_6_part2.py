# import copy

# start_row = 0
# start_col = 0
# for i in range(nrows):
#     for j in range(ncols):
#         if grid[i][j] == '^':
#             start_row = i
#             start_col = j
# print('start', start_row, start_col)
# starting pos 45, 42

# starting position in grid
def get_start_pos(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == '^':
                return i, j


# return true if obstruction creates a loop
def check_loop(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    row, col = get_start_pos(grid)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0  # intial direction going up
    x, y = dirs[dir_idx]
    seen = set()
    seen.add((row, col, dir_idx))

    while (0 <= row + x < nrows) and (0 <= col + y < ncols):
        if grid[row + x][col + y] == '#':  # change direction
            dir_idx = (dir_idx + 1) % 4
            x, y = dirs[dir_idx]
        else:
            row += x
            col += y
            if (row, col, dir_idx) not in seen:
                seen.add((row, col, dir_idx))
            else:
                return True
    return False


# loop_count = 0
# for i in range(nrows):
#     for j in range(ncols):
#         print(i, j)
#         grid = copy.deepcopy(grid_bak)
#         if grid[i][j] == '.':
#             grid[i][j] = '#'  # try all position for the obstruction
#             if check_loop(grid):
#                 loop_count += 1
# print(loop_count)
# 1812 incorrect

filename = 'aoc6data1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

grid = [[c for c in s] for s in texts]
nrows = len(grid)
ncols = len(grid[0])
# grid_bak = copy.deepcopy(grid)

loop_count = 0
for row in range(nrows):
    print(row)
    for col in range(ncols):
        if grid[row][col] == '.':
            # Create a copy of the grid with the current '.' replaced with '#'
            new_grid = [list(row) for row in grid]
            new_grid[row][col] = '#'
            if check_loop(new_grid):
                loop_count += 1
print(loop_count)
# 1911 - correct
