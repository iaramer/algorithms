"""
This problem is in "Very simple" group

In your research you are investigating an infinite series. To analyse it better, you want to calculate it's partial
sums for different parameters a, n:

sum(n,a) = sum([i*a**i for i in range(n)])

You also know that all partial sums you will need to calculate are less or equal to 1018.

Input format
Single line of input file contains two integer numbers 1 ≤ n, a ≤ 1018 — parameters of partial sum you want to
calculate. It is guaranteed that sum(n, a) ≤ 1018

Output format
Print single integer number: sum(n, a)
"""

DEBUG = True


def func1(n, a):
    # return sum([i * a ** i for i in range(1, n + 1)])
    l = [a]
    for i in range(1, n):
        l.append(l[i - 1] * a // i * (i + 1))
    return sum(l)


def func(n, a):
    if a == 1:
        return (1 + n) * n // 2
    else:
        return (n * a ** (n + 2) - n * a ** (n + 1) - a ** (n + 1) + a) // ((a - 1) ** 2)


if __name__ == '__main__':
    if DEBUG:
        res = func(2, 3)
        act = 21
        print(f'{res}, {act}')
        assert act == res

        res = func(3, 5)
        act = 430
        print(f'{res}, {act}')
        assert act == res

        res = func(1, 1000000)
        act = 1000000
        print(f'{res}, {act}')
        assert act == res

        res = func(1, 10 ** 18)
        act = 10 ** 18
        print(f'{res}, {act}')
        assert act == res

        res = func(1, 1)
        act = 1
        print(f'{res}, {act}')
        assert act == res

        res = func(10, 1)
        act = 55
        print(f'{res}, {act}')
        assert act == res
    else:
        n, a = map(int, input().split())
        print(func(n, a))
