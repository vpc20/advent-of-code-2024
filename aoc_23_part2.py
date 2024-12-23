from collections import defaultdict


def create_graph(conns):
    g = defaultdict(list)
    for conn in conns:
        v1, v2 = conn.split('-')
        # if v1[0] == 't' or v2[0] == 't':  # only starting with 't' is requiredd
        g[v1].append(v2)
        g[v2].append(v1)
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


def is_complete_graph(g, vertices):
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if j != i:
                if vertices[i] not in g[vertices[j]]:
                    return False
    return True
    # for vertex in vertices:
    #     for k in g.keys():
    #         if vertex != k and vertex not in g[k]:
    #             return False
    # return True


def solve_part2(input_conns):
    # count = 0
    g = create_graph(input_conns)
    comp_count = len(g.keys())
    print(comp_count)
    comp_list = sorted(list(g.keys()))
    print(comp_list)
    for i in range(comp_count, -1, -1):
        for j in range(0, comp_count - i + 1):
            sub_list = comp_list[j:i+j]
            print(sub_list)
            if is_complete_graph(g, sub_list):
                for i in range(len(sub_list)):
                    if sub_list[i][0] == 't':
                        # count += 1
                        return ','.join(sub_list)
    return None


f = open('aoc_23_test_data1.txt')
# f = open('aoc_23_data1.txt')
input_conns = [line.strip() for line in f]
# print(input_conns)
f.close()

x = solve_part2(input_conns)
print(x)
