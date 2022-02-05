"""
This problem is in "Normal" group

You are researching different DNAs. DNA is a sequence of nucleotides.
There are 4 types of nucleotides in DNA: cytosine [C], guanine [G], adenine [A] or thymine [T].

During your previous experiment you found out that you should not consider DNAs which contain at least 3 Adenine
nucleotides [A] in a row.

Now you want to calculate amount of different DNAs of N nucleotides which you still need to consider.
(Don't think about complementary sequence, just ignore complementarity rules).

Input format
Input file contains single integer number 0 < N ≤ 30.

Output format
Print single integer number: number of DNAs consisting of N nucleotides which doesn't have 3 As in a row.
"""

DEBUG = True


def func(n):
    dp = [[0] * 2, [0] * 2, [0] * 2]
    dp[0][1] = 3  # T, G, C
    dp[1][1] = 1  # A
    for i in range(2, n + 1):
        dp[0].append(3 * (dp[0][i - 1] + dp[1][i - 1] + dp[2][i - 1]))
        dp[1].append(dp[0][i - 1])
        dp[2].append(dp[1][i - 1])
    res = dp[0][n] + dp[1][n] + dp[2][n]
    return res


if __name__ == '__main__':
    if DEBUG:
        res = func(1)
        act = 4
        print(f'{res}, {act}')
        assert act == res

        res = func(3)
        act = 63
        print(f'{res}, {act}')
        assert act == res

        res = func(10)
        act = 947808
        print(f'{res}, {act}')
        assert act == res
    else:
        print(func(int(input())))
