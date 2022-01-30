"""
This problem is in "Very simple" group

During this year we had lots of troubles because of covid-19 pandemic. E.g. lockdowns and closed state borders. Many
travellers had to discard their abroad trips because of closed borders.

You are given number of cities (allover the world) and list of still opened roads connecting these cities. All the
roads are bidirectional. To help travellers allover the world, write a program which will be able to calculate for a
traveller the number of cities he/she still can visit from his home city.

Input format
First line contains three integer numbers divided by space character: 0 < N ≤ 100000, 0 ≤ M ≤ 100000, 0 ≤ s < N —
number of cities and roads and id of home city of current traveller respectively.

Each of next M lines contains two integer numbers vi, ui — ids of cities connected by i-th road: 0 ≤ vi, ui < N.

Output format
Print single integer number — number of cities reachable from city s (including city s itself).
"""

import sys
from collections import defaultdict

DEBUG = True


def read_cli(f):
    sys.stdin = open(f, 'r')
    N, M, s = map(int, input().split())
    roads = defaultdict(set)  # k - city, v - list of roads to other cities
    for _ in range(M):
        v, u = map(int, input().split())
        roads[v].add(u)
        roads[u].add(v)
    return roads, s


def func(d, s):
    return len(dfs(d, s, set()))


def dfs(d, s, v):
    adj_c = d[s] - v
    if len(adj_c) == 0:
        return set()
    for c in adj_c:
        v.add(c)
        v = v.union(dfs(d, c, v))
    return v


if __name__ == '__main__':
    if DEBUG:
        res = func(*read_cli('ex1.txt'))
        act = 3
        print(f'{res}, {act}')
        assert act == res

        res = func(*read_cli('ex2.txt'))
        act = 5
        print(f'{res}, {act}')
        assert act == res

        res = func(*read_cli('ex3.txt'))
        act = 5
        print(f'{res}, {act}')
        assert act == res

        res = func({1: {1}}, 1)
        act = 1
        print(f'{res}, {act}')
        assert act == res

        res = func({1: set()}, 1)
        act = 0
        print(f'{res}, {act}')
        assert act == res

        res = func({1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}}, 1)
        act = 4
        print(f'{res}, {act}')
        assert act == res

        res = func({1: {2}, 2: {3, 1}, 3: {4, 2}, 4: {3}}, 1)
        act = 4
        print(f'{res}, {act}')
        assert act == res

        res = func({1: {2, 4}, 2: {3, 1}, 3: {4, 2}, 4: {3, 1}}, 1)
        act = 4
        print(f'{res}, {act}')
        assert act == res

        res = func({1: set(), 2: set(), 3: set()}, 1)
        act = 0
        print(f'{res}, {act}')
        assert act == res
    else:
        print(func(*read_cli('input.txt')))
