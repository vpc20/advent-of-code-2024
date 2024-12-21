def update_grid(grid, row, col, dc, dr):
    str_row = row
    str_col = col
    while True:
        row += dr
        col += dc
        if grid[row][col] == '#':
            return False  # no update
        elif grid[row][col] == 'O':
            continue
        else:  # '.' encountered
            while not (row == str_row and col == str_col):
                grid[row][col], grid[row - dr][col - dc] = \
                    grid[row - dr][col - dc], grid[row][col]
                row = row - dr
                col = col - dc
            break
    return True


def sum_box_gps(grid):
    result = 0
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 'O':
                result += 100 * i + j
    return result


def solve_part1(grid, all_moves, row, col):
    for moves in all_moves:
        for m in moves:
            print('move', m)
            dr, dc = dir_dict[m]
            # if grid[row + dr][col + dc] == '#':
            #     for e in grid:
            #         print(''.join(e))
            #     continue
            # else:
            #     if update_grid(grid, row, col, dc, dr):
            #         row += dr
            #         col += dc
            if update_grid(grid, row, col, dc, dr):
                row += dr
                col += dc
            for e in grid:
                print(''.join(e))
    return sum_box_gps(grid)


# parse text input
filename = 'aoc15data1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
# arr = [[c for c in line.strip()] for line in inf]
# nums1 = [re.findall(r'-*\d+', line) for line in inf]
grid = [[c for c in line.strip()] for line in inf if line.startswith('#')]
inf.close()

inf = open(filename)
all_moves = [line.strip() for line in inf if line.startswith(('<', '>', '^', 'v'))]
inf.close()

for e in grid:
    print(''.join(e))
for moves in all_moves:
    print(moves)

# print(solve_part1(arr, 11, 7))
nrows = len(grid)
ncols = len(grid[0])

# find starting position
for i in range(nrows):
    for j in range(ncols):
        if grid[i][j] == '@':
            row = i
            col = j
            print('start row', i)
            print('start col', j)

dir_dict = {
    '<': (0, -1),
    '>': (0, +1),
    '^': (-1, 0),
    'v': (+1, 0)
}

print(solve_part1(grid, all_moves, row, col))
# 1552879
