"""
No legend. Just pure mathematics =)

Given an undirected graph G=(V, E). |V| = N, |E| = M.

V = {0, 1, ..., N - 1}

Find all connected components of this graph.

Input format
First line contains two integer numbers divided by space character: 0 < N ≤ 100000, 0 < M ≤ 100000 — number of
vertices and edges respectively.

Each of next M lines contains two integer numbers vi, ui — vertices connected by i-th edge: 0 ≤ vi, ui < N.
(Actually, it is just an edge list, described in the lecture).

Output format
On first line print only integer number — number of connected components in the graph.

Then, for each connected component print two lines:

1. Number of vertices in the component.

2. Numbers of vertices which construct this component divided by space character.

You are free to print components and vertices inside components in any order.
"""

import sys


def read_act(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


def read_cli(file):
    sys.stdin = open(file, 'r')
    N, M = map(int, input().split())
    G = [[] for i in range(N)]

    for i in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    return G


# def dfs(G, visited, v):  # recursive
#     if visited[v]:
#         return {}
#     visited[v] = True
#     nodes = {v}
#     if not G[v]:
#         return nodes
#     for node in G[v]:
#         if not visited[node]:
#             nodes = set.union(nodes, dfs(G, visited, node))
#     return nodes


def dfs(G, visited, v):  # non-recursive
    if visited[v]:
        return {}
    visited[v] = True
    nodes = {v}
    if not G[v]:
        return nodes
    to_visit = G[v]
    for node in to_visit:
        if not visited[node]:
            visited[node] = True
            nodes.add(node)
            if len(G[node]) > 0:
                to_visit += G[node]
    return nodes


def func(G):
    n_components = 0
    components = list()

    # calculating number of connected components:
    visited = [False] * len(G)
    for i in range(len(G)):
        if not visited[i]:
            n_components += 1
            components.append(dfs(G, visited, i))

    res = list()
    res.append(str(n_components))
    for c in components:
        res.append(str(len(c)))
        res.append(' '.join(list(map(str, c))))
    return res


if __name__ == '__main__':
    # for s in func(read_cli('input.txt')):
    #     print(s)

    act = read_act('act1.txt')
    res = func(read_cli('ex1.txt'))
    assert res == act

    act = read_act('act2.txt')
    res = func(read_cli('ex2.txt'))
    assert res == act

    act = read_act('act3.txt')
    res = func(read_cli('ex3.txt'))
    assert res == act

    act = read_act('act4.txt')
    res = func(read_cli('ex4.txt'))
    assert res == act

    act = read_act('act5.txt')
    res = func(read_cli('ex5.txt'))
    assert res == act

    print('OK')
