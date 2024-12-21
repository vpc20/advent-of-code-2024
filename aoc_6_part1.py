filename = 'aoc_6_test_data1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

grid = [[c for c in s] for s in texts]
nrows = len(grid)
ncols = len(grid[0])
row = 0
col = 0

for i in range(nrows):
    for j in range(ncols):
        if grid[i][j] == '^':
            row = i
            col = j
print('start', row, col)
# starting pos 45, 42

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
diri = 0  # direction index, intial direction going up
x, y = dirs[diri]
steps = 1

while (0 <= row + x < nrows) and (0 <= col + y < ncols):
    if grid[row + x][col + y] == '#':
        diri = (diri + 1) % 4
        x, y = dirs[diri]
    row += x
    col += y
    if grid[row][col] == '.':
        steps += 1
        grid[row][col] = 'X'

for e in grid:
    print(e)
print(steps)
# 4903
