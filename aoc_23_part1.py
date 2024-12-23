from collections import defaultdict
from itertools import combinations


def create_graph(conns):
    g = defaultdict(list)
    for conn in conns:
        v1, v2 = conn.split('-')
        # if v1[0] == 't' or v2[0] == 't':  # only starting with 't' is requiredd
        g[v1].append(v2)
        g[v2].append(v1)
    # print(len(g.keys()))
    # x = sorted(list(g.keys()))
    # print(','.join(x))
    return g


# def connected_components(g):
#     def dfs(g, u):
#         seen.add(u)
#         conns[-1].append(u)  # add to the last list
#         for v in g[u]:  # loop through all neighbors
#             if v not in seen:
#                 dfs(g, v)
#
#     conns = []
#     seen = set()
#     for u in g.keys():  # u is vertices
#         if u not in seen:
#             conns.append([])  # list of lists
#             dfs(g, u)
#     return conns


def is_complete_graph(g, combs):
    for i in range(3):
        for j in range(3):
            if j != i:
                if combs[i] not in g[combs[j]]:
                    return False
    return True
# def is_complete_graph(g, vertices):
#     for vertex in vertices:
#         for k in vertices:
#             if vertex not in g[k]:
#                 return False
#     return True


def solve_part1(input_conns):
    count = 0
    g = create_graph(input_conns)
    # all_conn_comps = connected_components(g)
    # print(all_conn_comps)

    for combs in combinations(g.keys(), 3):
        if is_complete_graph(g, combs):
            for i in range(3):
                if combs[i][0] == 't':
                    count += 1
                    # print('---combs')
                    # print(combs)
                    break
    return count


# f = open('aoc_23_test_data1.txt')
f = open('aoc_23_data1.txt')
in_conns = [line.strip() for line in f]
print(in_conns)
f.close()

x = solve_part1(in_conns)
print(x)

