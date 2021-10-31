"""
Time limit	3 seconds
Memory limit	256Mb
Input	standard input or input.txt
Output	standard output or output.txt

MSAI teachers continue to analyse results of this year courses. And again, they can't do without your help!

This time number of students was 0 ≤ N ≤ 100000, and teachers want to check if courses were too easy or too difficult.
To do that they need to check number of students whose average score is within given range: l ≤ score ≤ r.

Please, help the teachers and write the program which can process such requests fast. The number of requests teachers
prepared for you is 0 ≤ M ≤ 100000.

Input format
First line contains two integer numbers divided by space character: 0 ≤ N, M ≤ 100000 — number of students and requests
respectively. Second line contains N numbers divided by space character: scores of students. 0 ≤ si ≤ 109. Each of the
following M lines contains two integer numbers: lj, rj, divided by space character: 0 ≤ lj ≤ rj ≤ 109

Output format
For each request (lj, rj) print one integer number on separate line:
number of students who got score within requested range: |{i:l_j<=s_i<=r_j}|.
"""

import sys


def read_cli(file):
    sys.stdin = open(file, 'r')
    n, m = list(map(int, input().split()))
    s = list(map(int, input().split()))
    l = list()
    r = list()
    for i in range(m):
        l1, r1 = list(map(int, input().split()))
        l.append(l1)
        r.append(r1)
    return s, l, r


def func3(scores, left, right):
    sc = dict()
    for score in scores:
        if score not in sc:
            sc[score] = 0
        sc[score] += 1
    sc_keys = sorted(list(sc.keys()))  # sorted keys of scores

    lr_borders = [(el1, el2) for el1, el2 in zip(left, right)]
    borders_dict = dict()
    for i, els in enumerate(lr_borders):
        if els not in borders_dict:
            borders_dict[els] = [i]
        else:
            borders_dict[els].append(i)
    # lr_borders = sorted(lr_borders, key=cmp_to_key(compare))
    lr_borders_sorted = sorted(lr_borders)  # lose order

    l = r = 0  # idx in sc_keys
    ans1 = sc[sc_keys[0]] if len(sc_keys) > 0 else 0
    ans = [0] * len(lr_borders)
    for i in range(len(lr_borders_sorted)):
        l_border = lr_borders_sorted[i][0]
        r_border = lr_borders_sorted[i][1]
        while sc_keys[l] < l_border:
            ans1 -= sc[sc_keys[l]]
            l += 1
        while sc_keys[r] < r_border:
            r += 1
            ans1 += sc[sc_keys[r]]
        while sc_keys[r] > r_border and r > 0:
            ans1 -= sc[sc_keys[r]]
            r -= 1
        for idx in borders_dict[(l_border, r_border)]:
            ans[idx] = ans1

    return ans


def binsearch_left(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r


def binsearch_right(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return r


def func(scores, left, right):
    scores.sort()
    ans = list()
    for i in range(len(left)):
        r_index = binsearch_right(scores, right[i])
        l_index = binsearch_left(scores, left[i])
        ans1 = r_index - l_index
        ans.append(ans1)
    return ans


def func4(scores, left, right):
    sc = dict()
    for score in scores:  # O(n)
        if score not in sc:
            sc[score] = 0
        sc[score] += 1

    sc_keys = sorted(list(sc.keys()))  # sorted keys of scores
    if len(sc_keys) == 0:
        return [0] * len(left)
    if len(left) == 0:
        return []

    ansd = dict()
    ans = list()
    for i in range(len(left)):  # O(m)
        ans1 = 0
        l_border = left[i]
        r_border = right[i]
        if r_border > sc_keys[-1]:
            r_border = sc_keys[-1]
        if l_border < sc_keys[0]:
            l_border = sc_keys[0]
        if l_border > sc_keys[-1] or r_border < sc_keys[0]:
            ans.append(ans1)
            continue

        if (l_border, r_border) in ansd:
            ans1 = ansd[(l_border, r_border)]
        else:
            for k, v in sc.items():  # O(n)
                if l_border <= k <= r_border:
                    ans1 += v
            ansd[(l_border, r_border)] = ans1
        ans.append(ans1)
    return ans


def func2(scores, left, right):
    sc = [0] * (10 ** 9 + 1)
    for s in scores:
        sc[s] += 1

    ans = list()
    ansd = dict()
    for i in range(len(left)):
        ans1 = 0
        if (left[i], right[i]) in ansd:
            ans1 = ansd[(left[i], right[i])]
        else:
            ans1 += sum(sc[left[i]: right[i] + 1])
            ansd[(left[i], right[i])] = ans1
        ans.append(ans1)
    return ans


if __name__ == '__main__':
    res = func(*read_cli('ex1.txt'))
    act = [2, 3, 1, 5, 4, 6]
    assert res == act

    res = func(*read_cli('ex2.txt'))
    act = [0, 2, 0]
    assert res == act

    res = func(*read_cli('ex3.txt'))
    act = [1, 1, 2]
    assert res == act

    # n=0
    res = func([], [1, 2, 3], [1, 3, 3])
    act = [0, 0, 0]
    assert res == act

    res = func([1, 2, 3], [1, 1, 1], [1, 3, 1])
    act = [1, 3, 1]
    assert res == act

    # m=0
    res = func([1, 2, 3], [], [])
    act = []
    assert res == act

    # n=0, m=0
    res = func([], [], [])
    act = []
    assert res == act

    print('It\'s ok!')
