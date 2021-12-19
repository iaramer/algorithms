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

Second line contains two integer numbers: 0 ≤ s, h < N — number of the city you are in and number of your home city, .

Each of following M lines defines an edge  with weight wi and contains three integer numbers:
ui, vi, wi: 0 ≤ ui, vi < N, 0 ≤ wi leq 10000.

Output format
On the first line print weight of the optimal path  or -1 if path doesn't exist.

If path exists, the second line should contain number of vertices in the path k.

If path exists, the third line should contain k integer numbers — vertices in the optimal path in the order they will
be visited (first one is s, last one is h).
"""


def func():
    pass


if __name__ == '__main__':
    res = func()
    act = 30
    assert res == act

    res = func()
    act = 200
    assert res == act

    res = func()
    act = 1000
    assert res == act

    res = func()
    act = 4
    assert res == act
