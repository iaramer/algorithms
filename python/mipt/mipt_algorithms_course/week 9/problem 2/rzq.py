"""
After Lecture 9 on Algorithms and Data structures at MSAI, your are very interested in different range queries.

The last idea which interested you is RZQ. RZQ(l, r) — number of zeroes in the array in range [l, r):


You have found a dynamic (non-constant) array and are experimenting with it.
You want to check if it's possible to compute RZQ queries using  operations.

You have an initial array a which consists of N elements |ai| ≤ 104. You have requests of 2 types:

? l r — RZQ(l, r). 0 ≤ l < r ≤ N

or

+ i delta — inc(i, delta): increase a[i] value by delta. 0 ≤ i < N; |delta| < 104

Provide an answer for each "?" request.

Input format
First line contains two integer numbers: 0 < N, M ≤ 105 — number of items in array and number of requests.

Second line contains N integer numbers divided by space character: initial state of a array. |ai| ≤ 104.

Each of following M lines contain one character ("?" or "+") followed by two integer numbers.
This line describes a request:

? l r — RZQ(l, r). 0 ≤ l < r ≤ N

+ i delta — inc(i, delta). 0 ≤ i < N; |delta| < 104

Output format
For each "?" request print one integer number — answer for RZQ request.
"""

import sys
from math import log2, ceil

DEBUG = True


def read_cli(file):
    sys.stdin = open(file, 'r')
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    qs = [input().split() for _ in range(M)]
    return N, arr, qs


class RZQSegmentTree:
    neutral_value = 0

    def __init__(self, a):
        self.N = 2 ** int(ceil(log2(len(a))))
        neutral = [self.neutral_value] * (self.N - len(a))
        self.a = a
        self.a_zadj = [ai == 0 for ai in self.a]
        self.s = [None] * (self.N - 1) + list(self.a_zadj) + neutral
        for i in range(self.N - 2, -1, -1):
            self.refresh_s(i)

    def refresh_s(self, i):
        self.s[i] = self.s[2 * i + 1] + self.s[2 * i + 2]

    def rzq_i(self, l, r, i, li, ri):
        if (r <= li) or (ri <= l):
            return self.neutral_value
        if (l <= li) and (ri <= r):
            return self.s[i]
        middle = li + (ri - li) // 2
        rsq_l = self.rzq_i(l, r, i * 2 + 1, li, middle)
        rsq_r = self.rzq_i(l, r, i * 2 + 2, middle, ri)
        return rsq_l + rsq_r

    def update(self, i, v):
        self.a[i] += v
        self.a_zadj[i] = self.a[i] == 0
        j = i + self.N - 1
        self.s[j] = self.a_zadj[i]
        while j > 0:
            j = (j - 1) // 2
            self.refresh_s(j)

    def rzq(self, l, r):
        return self.rzq_i(l, r, 0, 0, self.N)


def func(N, arr, qs):
    rzq_tree = RZQSegmentTree(arr)
    ans = list()
    for a in qs:
        if a[0] == '?':
            l, r = int(a[1]), int(a[2])
            ans.append(rzq_tree.rzq(l, r))
        elif a[0] == '+':
            i, val = int(a[1]), int(a[2])
            rzq_tree.update(i, val)
    return ans


if __name__ == '__main__':
    if DEBUG:
        ans = func(*read_cli("ex1.txt"))
        act = [0, 1, 0, 1, 0]
        assert ans == act

        ans = func(*read_cli("ex2.txt"))
        act = [3, 2, 1, 0, 1]
        assert ans == act

        ans = func(*read_cli("ex3.txt"))
        act = [3, 2, 2, 3]
        assert ans == act

        print('OK!')
    else:
        for el in func(*read_cli("input.txt")):
            print(el)
