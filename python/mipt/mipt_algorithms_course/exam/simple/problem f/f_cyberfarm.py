"""
This problem is in "Simple" group

You were very impressed by Russian CyberFarm promotional movie https://www.youtube.com/watch?v=8HZ4DnVfWYQ and decided
to go to Mars to help them in colonization.

Your knowledge in algorithms will be very useful there. The first task for you is to install autowatering system for
fractal cucumbers. CyberFarm team is slightly terraforming Mars and changing the climate. For now they even have water
rains sometimes.

Cucumbers grow in 0 < N ≤ 108 special pots, which are situated on a straight line and enumerated from 0. Rains on Mars
are usually very short and localized. Each rain happens above some range of pots: [l, r). During this rain each pot
with index in range [l, r) obtain exactly 1 milliliter of water.

Fractal cucumbers need to be watered by exact amount of water, otherwise they won't be fractal enough. To satisfy this
limitation, before watering your system should analyse total amount of water pots in some region [l, r) already obtained
 from rain.

You are given list of rains during the current period. Also you are given queries from your watering system, which
request total amount of water obtained by pots in range [l, r).

Notice that all rains have already passed before the moment you calculate answers for queries. It is guaranteed that it
is not raining when you are doing that.

Input format
First line of input file contains 3 integer numbers: 0 < N ≤ 106; 0 ≤ M, K ≤ 105 — number of pots with cucumbers,
number of rains and number of requests respectively.
Each of next M lines contains two integer numbers li, ri describing i-th rain. 0 ≤ li ≤ ri < N.
Each of next K lines contains two integer numbers qli, qri, describing i-th query. 0 ≤ qli ≤ qri < N

Output format
For each query print single integer number on separate line: total amount of water obtained by pots with numbers in
range [l, r) because of rains (in milliliters).
"""

import sys

DEBUG = True


def read_cli(f):
    sys.stdin = open(f, 'r')
    N, M, K = map(int, input().split())
    rains = list()
    for _ in range(M):
        rains.append(tuple(map(int, input().split())))
    queries = list()
    for _ in range(K):
        queries.append(tuple(map(int, input().split())))
    return N, rains, queries


def func(N, rains, queries):
    pods = [0] * N
    for r in rains:
        if 0 <= r[0] < N:
            pods[r[0]] += 1
        if 0 <= r[1] < N:
            pods[r[1]] -= 1
    pfx = [0]
    pf = 0
    for i in range(1, N + 1):
        pf += pods[i - 1]
        pfx.append(pfx[i - 1] + pf)

    res = list()
    for q in queries:
        res.append(pfx[q[1]] - pfx[q[0]])
    return res


if __name__ == '__main__':
    if DEBUG:
        res = func(*read_cli('ex1.txt'))
        act = [5, 0, 3]
        print(f'{res}, {act}')
        assert act == res

        res = func(*read_cli('ex2.txt'))
        act = [4, 0]
        print(f'{res}, {act}')
        assert act == res

        res = func(*read_cli('ex3.txt'))
        act = [1000000]
        print(f'{res}, {act}')
        assert act == res
    else:
        for k in func(*read_cli('input.txt')):
            print(k)
