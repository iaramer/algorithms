"""
This problem is in "Simple" group

MSAI teachers ask you for help one more time. Now you are asked to generate standings table. You are given internal
logs of testing system. In these logs you have found file in which system prints login of the student when he/she
submits a correct (OK) solution of the problem he/she didn't solve successfully before.

Your problem should generate standings table according to the information from logs. Each line should contain student
login and number of problems solved by this student. Students should be sorted in descending order of the number of
solved problems. If two students have same number of solved problems, they should be printed in alphabetical order.

Input format
First line contains single integer number: 1 ≤ N ≤ 10000 — number lines in the log file.

Following N lines describe the log file. Each of these lines contains student login terminated by line break character.
Each login consists of 1-100 lowercase latin letters (a-z).

Output format
Your output should have N lines. Each should contain login of student followed by number of problems solved by this
student. Students should be sorted in descending order of the number of solved problems. If two students have same
number of solved problems, they should be printed in alphabetical order.
"""

import sys
from collections import Counter

DEBUG = True


def read_cli(f):
    sys.stdin = open(f, 'r')
    n = int(input())
    sts = list()
    for _ in range(n):
        sts.append(input())
    return sts


def func(studs):
    res = Counter(studs)
    return sorted(res.most_common(), key=lambda k: (-k[1], k[0]))


if __name__ == '__main__':
    if DEBUG:
        res = func(read_cli("ex1.txt"))
        act = [('kormen', 3)]
        print(f'{res}, {act}')
        assert act == res

        res = func(read_cli("ex2.txt"))
        act = [('dijkstra', 1), ('knuth', 1), ('kormen', 1)]
        print(f'{res}, {act}')
        assert act == res

        res = func(read_cli("ex3.txt"))
        act = [('dijkstra', 3), ('knuth', 2), ('kormen', 2)]
        print(f'{res}, {act}')
        assert act == res

        res = func(['koko'])
        act = [('koko', 1)]
        print(f'{res}, {act}')
        assert act == res

        res = func(['a', 'b', 'b'])
        act = [('b', 2), ('a', 1)]
        print(f'{res}, {act}')
        assert act == res
    else:
        for pair in func(read_cli('input.txt')):
            print(f'{pair[0]} {pair[1]}')
