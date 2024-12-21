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
    for e in conns:
        print(e)
    return conns


def count_corners(conns, coord):
    corner_ctr = 0
    r, c = coord

    # check neighbors to determine if the coordinate is a corner
    for d1, d2, d3 in ([(0, -1), (-1, 0), (-1, -1)],  # upper-left
                       [(-1, 0), (0, 1), (-1, 1)],  # upper-right
                       [(0, -1), (1, 0), (1, -1)],  # lower-left
                       [(0, 1), (1, 0), (1, 1)]):  # lower-right
        #  corner pointing out
        if (r + d1[0], c + d1[1]) not in conns and (r + d2[0], c + d2[1]) not in conns:
            corner_ctr += 1
        # corner pointing in
        if (r + d1[0], c + d1[1]) in conns and (r + d2[0], c + d2[1]) in conns and (r + d3[0], c + d3[1]) not in conns:
            corner_ctr += 1

    return corner_ctr


# def count_corners(conns, coord):
#     corner_ctr = 0
#     r, c = coord
#
#     # check neighbors to determine if the coordinate is a corner
#     if (r, c - 1) not in conns and (r - 1, c) not in conns:  # upper-left corner, pointing out
#         corner_ctr += 1
#     if (r, c - 1) in conns and (r - 1, c) in conns and (r - 1, c - 1) not in conns:  # upper-left corner, pointing in
#         corner_ctr += 1
#     if (r - 1, c) not in conns and (r, c + 1) not in conns:  # upper-right corner, pointing out
#         corner_ctr += 1
#     if (r - 1, c) in conns and (r, c + 1) in conns and (r - 1, c + 1) not in conns:  # upper-right corner, pointing in
#         corner_ctr += 1
#     if (r, c - 1) not in conns and (r + 1, c) not in conns:  # lower-left corner, pointing out
#         corner_ctr += 1
#     if (r, c - 1) in conns and (r + 1, c) in conns and (r + 1, c - 1) not in conns:  # lower-left corner, pointing in
#         corner_ctr += 1
#     if (r, c + 1) not in conns and (r + 1, c) not in conns:  # lower-right corner
#         corner_ctr += 1
#     if (r, c + 1) in conns and (r + 1, c) in conns and (r + 1, c + 1) not in conns:  # lower-right corner
#         corner_ctr += 1
#
#     return corner_ctr


def solve_part2(arr):
    g = create_graph(arr)
    all_conns = get_connected_components(g)

    total_price = 0
    for conns in all_conns:
        corner_ctr = 0
        for coord in conns:
            corner_ctr += count_corners(conns, coord)  # counting sides by counting corners
        total_price += len(conns) * corner_ctr
    return total_price


# parse text input
filename = 'aoc12data1.txt'
inf = open(filename)
# texts = [line.strip() for line in inf]
arr = [[c for c in line.strip()] for line in inf]
inf.close()

print(solve_part2(arr))
# 946084
