# from collections import defaultdict
import sys
from heapq import heappop, heappush


def dijkstra(grid, src, tgt):
    dists = {}  # distances
    preds = {}  # predecessors
    for r in range(nrows):
        for c in range(ncols):
            dists[(r, c)] = sys.maxsize
            preds[(r, c)] = None
    dists[src] = 0
    minq = [(0, src, 0, 0)]  # minimum priority queue - (distance, current position (r,c), direction, weight)

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # visited = set()
    # visited.add((0, src, 0, 0))

    while minq:
        estimate_dist, vertex, dir, wt = heappop(minq)
        r, c = vertex
        dir1 = dir  # going same direction
        dir2 = (dir - 1) % 4  # 90 degrees counter-clockwise
        dir3 = (dir + 1) % 4  # 90 degrees clockwise
        for nr, nc, ndir, nwt in [(r + dirs[dir1][0], c + dirs[dir1][1], dir1, 1),
                                  (r + dirs[dir2][0], c + dirs[dir2][1], dir2, 1001),
                                  (r + dirs[dir3][0], c + dirs[dir3][1], dir3, 1001)]:  # bfs, check for obstruction
            # if (nr, nc, ndir, nwt) in visited: continue
            if grid[nr][nc] != '#':
                estimate_dist = dists[vertex] + nwt
                if estimate_dist < dists[(nr, nc)]:  # relaxation
                    dists[(nr, nc)] = estimate_dist
                    preds[(nr, nc)] = vertex
                    heappush(minq, (estimate_dist, (nr, nc), ndir, nwt))
                    # visited.add((estimate_dist, (nr, nc), ndir, nwt))

    # for k, v in dists.items():
    #     print(k, v)
    print(dists[tgt])  # answer for part 1
    return dists, preds


# parse text input
filename = 'aoc16testdata1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
grid = [[c for c in line.strip()] for line in inf]
# nums1 = [re.findall(r'-*\d+', line) for line in inf]
inf.close()

for e in grid:
    print(''.join(e))

# print(solve_part1(grid, 11, 7))
nrows = len(grid)
ncols = len(grid[0])

# find starting position
for row in range(nrows):
    for col in range(ncols):
        if grid[row][col] == 'S':
            start_row = row
            start_col = col
            print('start row', start_row, '  start col', start_col)
        if grid[row][col] == 'E':
            end_row = row
            end_col = col
            print('end row', end_row, '  end col', end_col)

dijkstra(grid, (start_row, start_col), (end_row, end_col))

# part 2

