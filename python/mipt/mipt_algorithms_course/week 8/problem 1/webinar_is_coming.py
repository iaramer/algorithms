"""
Oups! This happened again!

Webinar on Algorithms and Data Structures is about to start, and you are still not at home.
In the previous problem (L7.B) you were rather close to home — you had just to go through park.
But now you are in the another city!

You've taken a taxi and driver asked you to show the way. You have a map of the country and you decided to use it to
find the shortest way home. Your map is rather simple: there is no roads which end in the same city they started in
and there's no more than one road between each pair of cities. All roads in your country are both-directional.

You are in a hurry, because you want to attend webinar with a cup of your favorite tea.

More formally: given simple undirected weighted graph and two vertices s, h. Find the weight of the shortest path and
sequence of vertices in any shortest path .

Input format
First line contains 2 integer numbers 2 ≤ N ≤ 100000, 1 ≤ M ≤ 200000 — number of cities (vertices) and roads (edges)
in the country (graph).

Second line contains two integer numbers: 0 ≤ s, h < N — number of the city you are in and number of your home city.

Each of following M lines defines an edge  with weight wi and contains three integer numbers:
ui, vi, wi: 0 ≤ ui, vi < N, 0 ≤ wi leq 10000.

Output format
On the first line print weight of the optimal path  or -1 if path doesn't exist.

If path exists, the second line should contain number of vertices in the path k.

If path exists, the third line should contain k integer numbers — vertices in the optimal path in the order they will
be visited (first one is s, last one is h).
"""

import math
import sys
from heapq import heappush, heappop

inf = math.inf
DEBUG = True


def read_cli(file):
    sys.stdin = open(file, 'r')
    N, M = map(int, input().split())
    start, end = map(int, input().split())
    G = [{} for i in range(N)]
    for i in range(M):
        u, v, weight = map(int, input().split())
        G[u][v] = weight
        G[v][u] = weight
    return N, M, start, end, G


def func(N, M, s, end, G):
    h = []
    d = [inf] * N
    v = -1
    shortest_nodes = [-1 for _ in range(N)]

    ans = list()
    S = {-1}
    d[s] = 0
    heappush(h, (d[s], s))
    while h:
        while v in S and h:
            v = heappop(h)[1]
        if v not in S:
            S.add(v)
            for u in G[v]:
                new_d = d[v] + G[v][u]
                if new_d < d[u]:
                    heappush(h, (new_d, u))
                    d[u] = new_d
                    shortest_nodes[u] = v
    if d[end] == inf:
        return [-1]
    ans.append(d[end])
    nodes = []
    while end != -1 and shortest_nodes:
        nodes.append(end)
        end = shortest_nodes[end]
    ans.append(len(nodes))
    ans.append(list(reversed(nodes)))
    return ans


if __name__ == '__main__':
    if DEBUG:
        res = func(*read_cli("ex1.txt"))
        act = [4, 4, [0, 1, 3, 2]]
        assert res == act

        res = func(*read_cli("ex2.txt"))
        act = [-1]
        assert res == act

        res = func(*read_cli("ex3.txt"))
        act = [13, 3, [0, 4, 2]]
        assert res == act

        print('OK!')
    else:
        res = func(*read_cli("input.txt"))
        print(res[0])
        if len(res) > 1:
            print(res[1])
            print(' '.join(str(n) for n in res[2]))
