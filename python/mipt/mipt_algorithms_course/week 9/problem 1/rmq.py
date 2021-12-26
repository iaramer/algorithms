"""
Implement data structure to support dynamic RMQ queries. Given initial array a with 0 < N ≤ 105 elements
and 0 < M ≤ 104 requests of 2 types:

? l r — RMQ(l, r)

+ i val — update(i, val) (a[i] := val)

Provide answer for each RMQ request.

Input format
First line contains two integer numbers: 0 < N ≤ 105;
0 < M ≤ 104 — number of elements in the array and number of requests.

Next line contains N integer numbers ai — elements of initial array, |ai| ≤ 105.

Each of following M lines contains request of one of 2 types:

? l r — RMQ(l, r). 0 ≤ l < r ≤ N

or

+ i val — update(i, val). 0 ≤ i < N; |val| < 105

Output format
For each "?" request provide answer — minimum value on requested range: RMQ(l, r)=min{a[i]: i∈ [l; r)}.
"""

import sys
from math import ceil, log2, inf

DEBUG = True


def read_cli(file):
    sys.stdin = open(file, 'r')
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    qs = [input().split() for _ in range(M)]
    return N, arr, qs


class RMQSegmentTree:
    neutral_value = inf

    def __init__(self, a):
        self.N = 2 ** int(ceil(log2(len(a))))
        neutral = ([self.neutral_value] * (self.N - len(a)))
        self.s = [None] * (self.N - 1) + list(a) + neutral
        for i in range(self.N - 2, -1, -1):
            self.refresh_s(i)

    def refresh_s(self, i):
        self.s[i] = min(self.s[2 * i + 1], self.s[2 * i + 2])

    def rmq_i(self, l, r, i, li, ri):
        if (r <= li) or (ri <= l):
            return self.neutral_value
        if (l <= li) and (ri <= r):
            return self.s[i]
        middle = li + (ri - li) // 2
        l_rmq = self.rmq_i(l, r, i * 2 + 1, li, middle)
        r_rmq = self.rmq_i(l, r, i * 2 + 2, middle, ri)
        return min(l_rmq, r_rmq)

    def update(self, i, v):
        i += self.N - 1
        self.s[i] = v
        while i > 0:
            i = (i - 1) // 2
            self.refresh_s(i)

    def rmq(self, l, r):
        return self.rmq_i(l, r, 0, 0, self.N)


def func(N, arr, qs):
    rmq_tree = RMQSegmentTree(arr)
    ans = list()
    for a in qs:
        if a[0] == '?':
            l, r = int(a[1]), int(a[2])
            ans.append(rmq_tree.rmq(l, r))
        elif a[0] == '+':
            i, val = int(a[1]), int(a[2])
            rmq_tree.update(i, val)
    return ans


if __name__ == '__main__':
    if DEBUG:
        ans = func(*read_cli("ex1.txt"))
        act = [5, 2]
        assert ans == act

        ans = func(*read_cli("ex2.txt"))
        act = [1, 2, 3, 2]
        assert ans == act

        ans = func(*read_cli("ex3.txt"))
        act = [1, 2]
        assert ans == act

        ans = func(*read_cli("ex4.txt"))
        act = [-1]
        assert ans == act

        print('OK!')
    else:
        for el in func(*read_cli("input.txt")):
            print(el)
