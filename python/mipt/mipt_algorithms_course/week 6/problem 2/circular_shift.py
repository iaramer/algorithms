"""
Given two strings s1 and s2. Check if s2 is a right circular shift of s1. If yes — print minimum non-negative K such
that CircShift(s1, K)=s2. If no — print -1.

b = CircShift(a, 1) just moves all elements to the right and replaces first element with the last one:



CircShift(a, K) just repeats this operation K times:


Input format
Input file contains two lines — strings s1 and s2 terminated by line break character. Both strings contain latin
letters only: (a-z, A-Z). Length of both strings do not exceed 100000: 0 < |s1| ≤ 100000, 0 < |s2| ≤ 100000.

Output format
Print single integer number K = min{k ≥ 0: CircShift(s1, k) = s2}, or -1 if K doesn't exist.
"""


def func(s1, s2):
    pass


if __name__ == '__main__':
    # print(func(input(), input()))

    res = func('abcde', 'eabcd')
    assert res == 1

    res = func('abcde', 'abcda')
    assert res == -1

    res = func('abcdefgh', 'fghabcde')
    assert res == 3
