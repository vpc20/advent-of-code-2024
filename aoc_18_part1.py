import sys
from heapq import heappop, heappush


def dijkstra(grid, src, tgt):
    dists = {}  # distances
    preds = {}  # predecessors
    for x in range(ncols):
        for y in range(nrows):
            dists[(x, y)] = sys.maxsize
            preds[(x, y)] = None
    dists[src] = 0
    minq = [(0, src)]  # minimum priority queue

    while minq:
        estimate_dist, vertex = heappop(minq)
        x, y = vertex
        for dx, dy in [(x, y + 1), (x + 1, y), (x, y - 1),
                       (x - 1, y)]:  # bfs, check for boundaries and obstruction
            if 0 <= dx < ncols and 0 <= dy < nrows and grid[dx][dy] != '#':
                estimate_dist = dists[vertex] + 1
                if estimate_dist < dists[(dx, dy)]:  # relaxation
                    dists[(dx, dy)] = estimate_dist
                    preds[(dx, dy)] = vertex
                    heappush(minq, (estimate_dist, (dx, dy)))
    print(dists)
    print()
    print(preds)
    print()
    # print(dists[(7, 7)])
    print(dists[(70, 70)])


# parse text input
filename = 'aoc18data1.txt'  # test - change
inf = open(filename)
# texts = [line.strip() for line in inf]
nums = [[int(e) for e in line.strip().split(',')] for line in inf]
# nums1 = [re.findall(r'-*\d+', line) for line in inf]
inf.close()

for e in nums:
    print(e)

nrows = 71  # test - change 7 to 71 later
ncols = 71  # test - change 7 to 71 later

grid = []
for i in range(nrows):
    grid.append(['.'] * ncols)

for e in grid:
    print(e)
print()

count = 1
for i, e in enumerate(nums):  # test
    if count <= 1024:  # test change 12 to 1024 later
        grid[e[1]][e[0]] = '#'
        count += 1
# for i, e in enumerate(nums):  # test
#     if e[0] < ncols and e[1] < nrows:
#         grid[e[1]][e[0]] = '#'
#         count += 1

for e in grid:
    print(e)

dijkstra(grid, (0, 0), (7, 7))  # test - change 7 to 71
# 340
