"""
Given string s: 0 < |s| ≤ 3000. Calculate number of distinct substrings in this string.

Input format
The single line contains string s: 0 < |s| ≤ 3000, which consists only of lowercase latin letters.
String is terminated with line break character.

Output format
Print single integer number — number of distinct substrings in the given string.

The answer is considered to be correct if it is given with asbolute error no more than 10:
"""

from random import randint


def c_to_i(ch):
    return ord(ch) - ord('a') + 1


DEBUG = True
p = 10 ** 9 + 7
a = randint(c_to_i('z') + 1, p - 1)


def func(s):
    n = len(s)
    if n == 0:
        return 0
    a_pow = [1] * (n + 1)
    for i in range(1, n + 1):
        a_pow[i] = (a_pow[i - 1] * a) % p
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] + c_to_i(s[i - 1]) * a_pow[i - 1]) % p
    res = 1
    for l in range(1, n):
        hs = set()
        for i in range(n - l + 1):
            cur_h = h[i + l] - h[i]
            cur_h = (cur_h * a_pow[n - i - l]) % p
            hs.add(cur_h)
        res += len(hs)
    return res


if __name__ == '__main__':
    if DEBUG:
        ans = func('abc')
        act = 6
        assert act == ans

        ans = func('aba')
        act = 5
        assert act == ans

        ans = func('aabaaba')
        act = 17
        assert act == ans

        ans = func('c')
        act = 1
        assert act == ans

        print('OK')
    else:
        print(func(input()))
