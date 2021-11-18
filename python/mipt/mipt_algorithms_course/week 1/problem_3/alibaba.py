"""
Ali Baba successfully brought treasures you helped him to choose in Ali Baba 1 Problem.
Now he returned back to cave with treasures again and this time he has taken a very big bag
to be able to take more treasures.

When he entered the cave, he found a room in it that contains 0 ≤ N ≤ 100000 bunches of golden sand.

For each bunch of sand, Ali Baba estimated it's weight (in grams) and it's cost
(he counts cost in dollars, because he loves green color).

His bag can hold not more than 0 ≤ W ≤ 10^9 grams of sand in total.

Also, Ali Baba counts cost of each bunch or it's part to be an integer number of dollars.
He do not take cents into account. He doesn't like cents, because they are not green.

Help Ali Baba to take out as many golden sand as he can, and maximize total cost.

Input format
First line contains two integer numbers divided by space character:
0 ≤ N ≤ 10^5 and 0 ≤ W ≤ 10^9 — number of bunches of golden sand and carrying capacity of a bag in grams respectively.

Next N lines contain information about bunches of golden sand. Each line contains two integer numbers:
0 ≤ ci ≤ 10^9 and 0 ≤ wi ≤ 10^9 — cost ($) and weight (g) of i-th bunch respectively.

Output format
Single integer number — maximum total cost in dollars of golden sand that Ali Baba can take out of the cave.

Example 1
Input
3 2
10 1
5 1
1000 2
Output
1000

Example 2
Input
1 100
400 300
Output
133

Example 3
Input
4 3
10 3
4 1
4 1
4 1
Output
12
"""


def qsort(arr):
    if len(arr) <= 1:
        return arr
    pi = len(arr) // 2
    r = list()
    l = list()
    m = list()
    for i in range(len(arr)):
        if arr[i][0] == arr[pi][0]:
            m.append(arr[i])
        if arr[i][0] < arr[pi][0]:
            r.append(arr[i])
        if arr[i][0] > arr[pi][0]:
            l.append(arr[i])
    return qsort(l) + m + qsort(r)


def ali_count(weight_capacity, bunches):
    ans = 0
    gram_costs = list()
    for gs in bunches:
        if gs[1] == 0:
            ans += gs[0]
        else:
            # (cost/weight, cost, weight)
            gram_costs.append((gs[0] / gs[1], gs[0], gs[1]))

    # sort by cost/weight
    gram_costs = qsort(gram_costs)

    # cumulative sum until there is no free space
    for i in range(len(gram_costs)):
        if weight_capacity >= gram_costs[i][2]:
            ans += gram_costs[i][1]
            weight_capacity -= gram_costs[i][2]
            if weight_capacity == 0:
                break
        else:
            ans += int(gram_costs[i][0] * weight_capacity)
            break

    return ans


if __name__ == '__main__':
    # n, w = map(int, input().split())
    # arr = list()
    # for _ in range(n):
    #     cost, weight = map(int, input().split())
    #     arr.append((cost, weight))
    # res = ali_count(w, arr)
    # print(res)

    inp = (2, [(10, 1), (5, 1), (1000, 2)])
    ans = ali_count(*inp)
    act = 1000
    assert ans == act

    inp = (100, [(400, 300)])
    ans = ali_count(*inp)
    act = 133
    assert ans == act

    inp = (3, [(10, 3), (4, 1), (4, 1), (4, 1)])
    ans = ali_count(*inp)
    act = 12
    assert ans == act

    inp = (3, [(10, 3), (4, 1), (4, 1), (1, 0), (4, 1)])
    ans = ali_count(*inp)
    act = 13
    assert ans == act

    inp = (0, [(10, 3), (4, 1), (4, 1), (4, 1)])
    ans = ali_count(*inp)
    act = 0
    assert ans == act

    inp = (0, [(10, 3), (4, 0), (4, 1), (1, 0), (4, 1)])
    ans = ali_count(*inp)
    act = 5
    assert ans == act

    inp = (0, [(0, 0), (0, 0), (0, 0)])
    ans = ali_count(*inp)
    act = 0
    assert ans == act

    inp = (1000, [(1, 1), (1, 1), (1, 1)])  # was RE, now WA
    ans = ali_count(*inp)
    act = 3
    assert ans == act

    inp = (1000, [(1, 1), (1, 1), (1, 1), (0, 1000)])
    ans = ali_count(*inp)
    act = 3
    assert ans == act

    inp = (1000, [(1, 1), (1, 1), (1, 1), (0, 1000)])
    ans = ali_count(*inp)
    act = 3
    assert ans == act

    inp = (1, [])
    ans = ali_count(*inp)
    act = 0
    assert ans == act

    inp = (1, [(1, 0), (1, 0), (1, 0), (1, 0)])
    ans = ali_count(*inp)
    act = 4
    assert ans == act

    inp = (0, [(1, 0), (1, 0), (1, 0), (1, 0)])
    ans = ali_count(*inp)
    act = 4
    assert ans == act

    inp = (1, [(1000, 3)])
    ans = ali_count(*inp)
    act = 333
    assert ans == act

    inp = (1000, [(500, 500), (100, 100), (100, 100)])
    ans = ali_count(*inp)
    act = 700
    assert ans == act

    print('It\'s ok!')
