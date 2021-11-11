"""
You have found a wooden board with N nails on a straight line in it. The first thing you did with it — you've measured
distance from to each nail to intersection of edge of the board and straight line on which nails are situated
(coordinates of each nail). Just because you're a scientist!

Also, you have a thread and you can connect each pair of nails with it. You want to connect several pairs of nails so
that each nail has at least one connection. Also, you don't want to waste thread, so, you want to minimize total
length of thread used for that.

Input format
First line contains one integer number 2 ≤ N ≤ 1000 — number of nails.

Second line contains N integer numbers divided by space character — coordinates of each nail 0 ≤ xi ≤ 10000.

Output format
Print one integer number — minimum total length of thread you need to connect nails such that each nail has at least
one connection.
"""


def func(arr):
    pass


if __name__ == '__main__':
    # n = input()
    # l = list(map(int, input().split()))
    # print(func(l))

    inp = [1, 2, 3]
    act = 2
    assert func(inp) == act

    inp = [11, 1, 2, 3]
    act = 9
    assert func(inp) == act

    inp = [0, 2, 10, 1, 12]
    act = 4
    assert func(inp) == act
