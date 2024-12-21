from collections import defaultdict


def create_graph(arr):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(arr)
    ncols = len(arr[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if arr[r][c] == arr[nr][nc]:
                        g[(r, c)].append((nr, nc))
            else:
                _ = g[(r, c)]  # create empty list, use _ instead of dummy variable
    return g


def get_connected_components(g):
    def dfs(g, u):
        seen.add(u)
        conns[-1].append(u)  # add to the last list
        for v in g[u]:  # loop through all neighbors
            if v not in seen:
                dfs(g, v)

    conns = []
    seen = set()
    for u in g.keys():  # u is vertices
        if u not in seen:
            conns.append([])  # list of lists
            dfs(g, u)
    return conns


def count_sides(conn, coord, nrows, ncols):
    side_count = 4
    r, c = coord
    for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
        if 0 <= nr < nrows and 0 <= nc < ncols:
            if (nr, nc) in conn:
                side_count -= 1
    return side_count


def solve_part1(arr):
    nrows = len(arr)
    ncols = len(arr[0])

    g = create_graph(arr)
    conns = get_connected_components(g)

    total_price = 0
    for conn in conns:
        perimeter = 0
        for coord in conn:
            perimeter += count_sides(conn, coord, nrows, ncols)
        total_price += len(conn) * perimeter
    return total_price


# parse text input
filename = 'aoc12data1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
arr = [[c for c in line.strip()] for line in inf]
inf.close()

print(solve_part1(arr))
# 1550156
