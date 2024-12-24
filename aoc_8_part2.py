from collections import defaultdict


def get_antinodes(coord1, coord2):
    anti_count = 0
    # antinodes_found = False
    # print('coords', (coord1, coord2))
    svx1, svy1 = coord1
    svx2, svy2 = coord2
    x1, y1 = coord1
    x2, y2 = coord2
    while 0 <= x1 < nrows and 0 <= y1 < ncols:
        x1, x2 = 2 * x1 - x2, x1
        y1, y2 = 2 * y1 - y2, y1
        if 0 <= x1 < nrows and 0 <= y1 < ncols:
            if (x1, y1) not in seen:
                # print((x1, y1))
                print((y1, x1))  # for comparison with other solution, y,x
                anti_count += 1
                seen.add((x1, y1))
                seen.add((svx1, svy1))  # include antennas in count, exclude duplicates
                seen.add((svx2, svy2))  # include antennas in count, exclude duplicates
                # antinodes_found = True

    svx1, svy1 = coord1
    svx2, svy2 = coord2
    x1, y1 = coord1
    x2, y2 = coord2
    while 0 <= x2 < nrows and 0 <= y2 < ncols:
        x2, x1 = 2 * x2 - x1, x2
        y2, y1 = 2 * y2 - y1, y2
        if 0 <= x2 < nrows and 0 <= y2 < ncols:
            if (x2, y2) not in seen:
                # print((x2, y2))
                print((y2, x2))  # for comparison with other solution, y,x
                anti_count += 1
                seen.add((x2, y2))
                seen.add((svx1, svy1))  # include antennas in count, exclude duplicates
                seen.add((svx2, svy2))  # include antennas in count, exclude duplicates
                # antinodes_found = True

    return len(seen)


# filename = 'aoc_8_test_data1.txt'
filename = 'aoc_8_data1.txt'
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

print(seen)
print(len(seen))
# print(total_count) - total_count is not the answer

# print(get_antinodes((1, 8), (2, 5)))
# print(get_antinodes((2, 5), (3, 7)))

# print(get_antinodes((0, 0), (1, 3)))
# print(get_antinodes((1, 3), (2, 1)))
# print(get_antinodes((0, 0), (2, 1)))
# print(get_antinodes((8, 8), (9, 9)))

# missing
# {(36, 34), (26, 17), (7, 0), (30, 0), (34, 38), (47, 6), (0, 25), (29, 47), (43, 44), (49, 17)}
