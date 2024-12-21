from collections import defaultdict


def get_antinodes(coord1, coord2):
    anti_count = 0
    # print('coords', (coord1, coord2))
    x1, y1 = coord1
    x2, y2 = coord2
    dx = x1 - x2
    dy = y1 - y2
    x = x1
    y = y1
    while 0 <= x < nrows and 0 <= y < ncols:
        seen.add((x1, y1))
        x += dx
        y += dy
    return len([0 for x,y in seen if 0 <= x < nrows and 0 <= y < ncols])


filename = 'aoc8testdata1.txt'
inf = open(filename)
texts = [line.strip() for line in inf]
inf.close()

grid = [[c for c in s] for s in texts]
nrows = len(grid)
ncols = len(grid[0])

fdict = defaultdict(list)
for i in range(nrows):
    for j in range(ncols):
        if grid[i][j] != '.':
            fdict[grid[i][j]].append((i, j))

for k, v in fdict.items():
    print(k, v)

seen = set()
total_count = 0
for v in fdict.values():
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            total_count += get_antinodes(v[i], v[j])

print(total_count)

# print(get_antinodes((1, 8), (2, 5)))
# print(get_antinodes((2, 5), (3, 7)))

# print(get_antinodes((0, 0), (1, 3)))
# print(get_antinodes((1, 3), (2, 1)))
# print(get_antinodes((0, 0), (2, 1)))
# print(get_antinodes((8, 8), (9, 9)))
