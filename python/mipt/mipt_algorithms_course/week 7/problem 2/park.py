"""
You're in a hurry, because webinar on Algorithms and Data structures is about to start. On your way home there is a
park and you decided to go this park through. And you want to find the shortest way from the enter
(your current position) to the exit.

Fortunately, you've found a map of the park. This may help.

Map of the park is square array of the following characters:

. – empty space (you can go through it)

# – barrier, e.g. a tree (you can't go through it)

E – your current position (Enter)

X – your destination (eXit)

From position (i, j) you can move to one of the (i - 1, j), (i, j - 1), (i + 1, j) or (i, j + 1) only if there's no
barrier in target position.

Input format
The first line contains two integer numbers: 0 < N ≤ 500, 0 < M ≤ 500 — number of rows and columns in the map
respectively.

Each of the next N lines contains M characters each (terminated with line break character) and denote a map of the park.

It is guaranteed that there are exactly one E and exactly one X characters in the map.

Output format
Print one integer number — minimum number of steps you need to get from the current position to the exit. If it is
impossible, print -1.
"""

import sys


def read_cli(file):
    sys.stdin = open(file, 'r')
    N, M = list(map(int, input().split()))
    mp = list()
    for _ in range(N):
        mp.append(list(input()))
    return mp


def is_valid(map, x, y):
    return 0 <= x < len(map) and 0 <= y < len(map[0])


def func(mp):
    x, y = 0, 0
    for i in range(len(mp)):
        for j in range(len(mp[i])):
            if mp[i][j] == 'E':
                x, y = i, j
                break

    mp[x][y] = '#'
    step = 1
    steps = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    nxt_steps = []
    while steps:
        x1, y1 = steps.pop()
        if not is_valid(mp, x1, y1) or mp[x1][y1] == '#':
            if not steps and len(nxt_steps) > 0:
                step += 1
                steps = nxt_steps
                nxt_steps = []
            continue
        if mp[x1][y1] == 'X':
            return step
        nxt_steps += [(x1 + 1, y1), (x1, y1 + 1), (x1 - 1, y1), (x1, y1 - 1)]
        mp[x1][y1] = '#'
        if not steps and len(nxt_steps) > 0:
            step += 1
            steps = nxt_steps
            nxt_steps = []
    return -1


if __name__ == '__main__':
    # print(func(read_cli('ex1.txt')))

    act = 2
    ans = func(read_cli('ex1.txt'))
    assert (act == ans)

    act = 7
    ans = func(read_cli('ex2.txt'))
    assert (act == ans)

    act = -1
    ans = func(read_cli('ex3.txt'))
    assert (act == ans)

    print('OK!')
