"""
You are given sequence x which contains 0 ≤ N ≤ 105 integer numbers: 0 ≤ xi < 10000. You need to calculate length of
Longest Increasing Subsequence of this sequence.

Increasing subsequence of sequence x = x0, x1, ..., xN-1 is:


You need to find maximum possible K.
Input format
First line of input file contains single integer number: 0 ≤ N ≤ 105 — length of initial sequence.

Second line contains N integer numbers divided by space character: 0 ≤ xi < 10000 — initial sequence.

Output format
Print single integer number K — length of longest increasing subsequence in x.
"""


def bin_search(x, arrs):
    l, r = 0, len(arrs)
    while r - l > 1:
        mid = (l + r) // 2
        if x < arrs[mid][-1]:
            r = mid
        else:
            l = mid
    return l


def func1(arr):  # Memory-greedy
    if len(arr) < 2:
        return len(arr)
    tails = []
    for x in arr:
        if len(tails) == 0:
            tails.append([x])
        elif x > tails[-1][-1]:
            tails.append(tails[-1] + [x])
        else:
            idx = bin_search(x, tails)
            if tails[idx][-1] > x:
                if idx == 0:
                    tails[idx][-1] = x
                elif tails[idx][-2] < x:
                    tails[idx][-1] = x
            elif idx + 1 < len(tails) and \
                    x < tails[idx + 1][-1] and x != tails[idx][-1]:
                tails[idx + 1] = tails[idx] + [x]
    return len(tails[-1])


def func(arr):
    if len(arr) < 2:
        return len(arr)
    tails = []
    for x in arr:
        if len(tails) == 0:
            tails.append([x])
        elif x > tails[-1][-1]:
            tails.append([tails[-1][-1], x])
        else:
            idx = bin_search(x, tails)
            if tails[idx][-1] > x:
                if idx == 0:
                    tails[idx][-1] = x
                elif tails[idx][-2] < x:
                    tails[idx][-1] = x
            elif idx + 1 < len(tails) and \
                    x < tails[idx + 1][-1] and x != tails[idx][-1]:
                tails[idx + 1] = [tails[idx][-1], x]
    return len(tails)


if __name__ == '__main__':
    # n = input()
    # arr = list(map(int, input().split()))
    # print(func(arr))

    inp = [1, 3, 4]
    act = 3
    assert func(inp) == act

    inp = [2, 1, 3, 4, 2]
    act = 3
    assert func(inp) == act

    inp = [3, 4, 2, 1, 3, 4, 2]
    act = 3
    assert func(inp) == act

    inp = []
    act = 0
    assert func(inp) == act

    inp = [111]
    act = 1
    assert func(inp) == act

    inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    act = 9
    assert func(inp) == act

    inp = list(reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    act = 1
    assert func(inp) == act

    inp = [1, 1, 1, 1, 1, 1]
    act = 1
    assert func(inp) == act

    inp = [0, 1, 0, 3, 2, 3]
    act = 4
    assert func(inp) == act

    inp = [10, 9, 2, 5, 3, 7, 101, 18]
    act = 4
    assert func(inp) == act

    inp = [4, 10, 4, 3, 8, 9]
    act = 3
    assert func(inp) == act

    print('OK')
