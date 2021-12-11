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