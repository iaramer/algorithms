"""
Time limit	1 second
Memory limit	256Mb
Input	standard input or input.txt
Output	standard output or output.txt
MSAI teachers are organizing an exam in another university and they are worried about cheating possibility.
Of course, this exam is not in MSAI and not in MIPT, because MIPT students do not cheat. Usually :)

So, teachers decided to prepare sitting places for examinees on a straight line, to be able to see them all.
Also, to minimize possibility of using each other's solutions, teachers want to maximize minimum distance between
students. Help them, please!

Classroom has 2≤ N ≤ 10000 sitting places, which are situated on a straight line. Their coordinates are 0 ≤ xi ≤ 109.
You need to assign M students to seats (choose M seats: xk1, xk2, ..., xkM) such that minimum distance between students
is as much as possible:

min{i!=j}|x_k_i - x_k_j| -> max

Write a program which will do that.

Input format
First line contains 2 integer numbers N, M divided by space character: 2 ≤ N ≤ 10000, 2 ≤ M ≤ N — number of sitting
places and students respectively.

Next line contains N integer numbers 0 ≤ xi ≤ 109 — coordinates of sitting places.

Output format
Print single integer number — desired maximized minimum distance:
"""

import sys


def read_cli(file):
    sys.stdin = open(file, 'r')
    n, m = list(map(int, input().split()))
    x = list(map(int, input().split()))
    return n, m, x


def is_feasible(mid, arr, n, m):
    pos = arr[0]
    elements = 1
    for i in range(1, n):
        if arr[i] - pos >= mid:
            pos = arr[i]
            elements += 1
            if elements == m:
                return True
    return False


def func(n, m, x):
    """
    :param n: Sitting places, 2 <= n <= 10000.
    :param m: Number of students, 2 ≤ m ≤ n.
    :param x: integer numbers - coordinates of sitting places, len(x) = n.
    :return: maximized distance.
    """
    x.sort()
    ans = -1
    left = 0
    right = x[-1]
    while left < right:
        mid = (left + right) // 2
        if is_feasible(mid, x, n, m):
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid
    return ans


if __name__ == '__main__':
    res = func(*read_cli('ex1.txt'))
    act = 1
    assert res == act

    res = func(*read_cli('ex2.txt'))
    act = 7
    assert res == act

    res = func(*read_cli('ex3.txt'))
    act = 11
    assert res == act

    # # n=0
    # res = func([], [1, 2, 3], [1, 3, 3])
    # act = [0, 0, 0]
    # assert res == act

    print('It\'s ok!')
