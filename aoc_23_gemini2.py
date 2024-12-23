from collections import defaultdict


def find_maximum_clique_bron_kerbosch(graph, R, P, X):
    """
    Finds the maximum clique in the graph using the Bron-Kerbosch algorithm.

    Args:
      graph: A dictionary representing the graph.
      R: Current clique.
      P: Potential vertices to add to the clique.
      X: Candidates that cannot be added to the clique.

    Returns:
      A set of computers in the maximum clique.
    """
    if not P and not X:
        if len(R) > len(find_maximum_clique_bron_kerbosch.max_clique):
            find_maximum_clique_bron_kerbosch.max_clique = R.copy()
        return

    if P:
        pivot = next(iter(P))  # Select a pivot vertex (e.g., the first one)
        for v in P - graph[pivot]:
            find_maximum_clique_bron_kerbosch(graph, R.copy(), P & graph[v], X & graph[v])
            P.remove(v)
            X.add(v)


find_maximum_clique_bron_kerbosch.max_clique = set()


def find_maximum_clique(connections):
    """
    Finds the largest clique in the graph.

    Args:
      connections: A list of strings, where each string represents a connection
                    between two computers in the format "computer1-computer2".

    Returns:
      A set of computers in the maximum clique.
    """

    graph = defaultdict(set)
    for connection in connections:
        computer1, computer2 = connection.split('-')
        graph[computer1].add(computer2)
        graph[computer2].add(computer1)

    vertices = set(graph.keys())
    find_maximum_clique_bron_kerbosch(graph, set(), vertices, set())
    return find_maximum_clique_bron_kerbosch.max_clique


# Example usage
connections = [
    "kh-tc",
    "qp-kh",
    "de-cg",
    "ka-co",
    "yn-aq",
    "qp-ub",
    "cg-tb",
    "vc-aq",
    "tb-ka",
    "wh-tc",
    "yn-cg",
    "kh-ub",
    "ta-co",
    "de-co",
    "tc-td",
    "tb-wq",
    "wh-td",
    "ta-ka",
    "td-qp",
    "aq-cg",
    "wq-ub",
    "ub-vc",
    "de-ta",
    "wq-aq",
    "wq-vc",
    "wh-yn",
    "ka-de",
    "kh-ta",
    "co-tc",
    "wh-qp",
    "tb-vc",
    "td-yn"
]

maximum_clique = find_maximum_clique(connections)
password = ','.join(sorted(maximum_clique))

print("Password:", password)  # Output: co,de,ka,ta
#incorrect
