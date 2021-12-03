"""
Given two strings s and s2. Check if s2 is a right circular shift of s. If yes — print minimum non-negative K such
that CircShift(s, K)=s2. If no — print -1.

b = CircShift(a, 1) just moves all elements to the right and replaces first element with the last one:



CircShift(a, K) just repeats this operation K times:


Input format
Input file contains two lines — strings s and s2 terminated by line break character. Both strings contain latin
letters only: (a-z, A-Z). Length of both strings do not exceed 100000: 0 < |s| ≤ 100000, 0 < |s2| ≤ 100000.

Output format
Print single integer number K = min{k ≥ 0: CircShift(s, k) = s2}, or -1 if K doesn't exist.
"""


def circ_shift(s, k):
    return s[k:] + s[:k]


def func(s1, s2):
    if len(s1) != len(s2) or len(s1) < 2:
        return -1

    s = s1 + s2
    d = [0] * (len(s) + 1)
    for i in range(2, len(d)):
        d[i] = d[i - 1]
        while s[i - 1] != s[d[i]] and d[i] > 0:
            d[i] = d[d[i]]
        if s[i - 1] == s[d[i]]:
            d[i] += 1

    if circ_shift(s1, d[-1]) == s2:
        return len(s1) - d[-1]

    return -1


if __name__ == '__main__':
    # print(func(input(), input()))

    res = func('abcde', 'eabcd')
    assert res == 1

    res = func('abcde', 'abcda')
    assert res == -1

    res = func('abcdefgh', 'fghabcde')
    assert res == 3

    res = func('a', 'a')
    assert res == -1

    res = func('123456', '612345')
    assert res == 1

    print('OK!')
