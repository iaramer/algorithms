"""
This problem is in "Hard" group

One famous Korean company, which is famous by it's smartphones and skyscrapers (e.g. Burj Khalifa) needs your help.

Company wants to build two skyscrapers of identical height. Skyscrapers will have main pillar in the middle.
This pillar should go vertically through each level (floor) of each skyscraper. Company already has materials for
these pillars. These materials are N undividable parts of the pillar, i-th part has a height of hi levels (floors).
Company wants the total height (number of levels) of pillars for both skyscrapers to be identical and as big as
possible.

Help company to choose parts of pillars which will allow both pillars to have maximum identical height.

Input format
First line of input file contains single integer number 0 < N ≤ 50 — number of parts of pillars.

Second line contains N integer numbers divided by space character: 0 < hi ≤ 7 — height of i-th part of the pillar.

Output format
On the first line print desired maximum height of both pillars.

On the second line print number of parts to be used for the first skyscraper.

On the third line print indices of parts to be used for the first skyscraper.

On the fourth line print number of parts to be used for the second skyscraper.

On the fifth line print indices of parts to be used for the second skyscraper.

If there are several ways to provide desired height — you can print any one.
You can print indices of parts in any order.
"""

from collections import defaultdict

DEBUG = True


def sep(pills, sum):
    """ Groups the pills into 2 groups with the given sum of each of the groups. """
    first, second = 0, 0


def func(n, pills):
    arr = defaultdict(int)  # Map from difference to best value of subset sum 1
    arr[0] = 0  # We start with a difference of 0

    for i, pill in enumerate(pills):
        arr2 = defaultdict(int)

        def add(s1, s2):
            if s1 > s2:
                s1, s2 = s2, s1
            d = s2 - s1
            if d in arr2:
                arr2[d] = max(arr2[d], s1)
            else:
                arr2[d] = s1

        for diff, sum1 in arr.items():
            sum2 = sum1 + diff
            add(sum1, sum2)  # Ignore the current element
            add(sum1 + pill, sum2)  # including element in partition 1
            add(sum1, sum2 + pill)  # including element in partition 2
        arr = arr2

        first, second = 0, 0  # number of pills in the first building and in the second one
    return arr[0], first, second


if __name__ == '__main__':
    if DEBUG:
        res = func(5, [2, 3, 5, 1, 2])
        act = 5
        print(f'{res}, {act}')
        assert act == res

        res = func(6, [2, 3, 5, 1, 2, 3])
        act = 8
        print(f'{res}, {act}')
        assert act == res

        res = func(7, [1, 1, 1, 1, 1, 1, 1])
        act = 3
        print(f'{res}, {act}')
        assert act == res
    else:
        n = int(input())
        pills = map(int, input().split())
        func(n, pills)

        # On the first line print desired maximum height of both pillars.

        # On the second line print number of parts to be used for the first skyscraper.

        # On the third line print indices of parts to be used for the first skyscraper.

        # On the fourth line print number of parts to be used for the second skyscraper.

        # On the fifth line print indices of parts to be used for the second skyscraper.
