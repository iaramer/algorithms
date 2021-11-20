"""
Ali Baba returned back to cave, and took his knapsack with carrying capacity  to take treasures out of the cave.
When he came into cave he found a room with  gold bars in it. For each bar he knows weight  and cost . As usual, he
wants to maximize total cost of treasures taken out. The bars are undividable.

Help Ali Baba and write a program which will calculate maximum obtainable profit and gives indices of items
(items are enumerated from 1) he should place into knapsack to maximize total cost.

Input format
First line contains two integer numbers:  and  — carrying capacity of knapsack and number of items in the cave.

Second line contains N positive integer numbers w1, w2, ..., wN, divided by space character — weights of items.

Third line contains N positive integer numbers c1, c2, ..., cN, divided by space character — costs of elements.

Output format
- On the first line print maximum total cost of bars Ali Baba can place into knapsack.

- On the second line print number of items K which allow to maximize total cost.

- On the third line print K positive integer numbers separated by space character — indices of items which maximize
total cost. Items are enumerated from 1!
"""

import sys


def read_cli(file):
    sys.stdin = open(file, 'r')
    w, n = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    return w, n, weights, costs


def func(weight, n, weights, costs):
    # maximum total cost
    d = [[0] * (weight + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, weight + 1):
            if weights[i - 1] > w:
                d[i][w] = d[i - 1][w]
            else:
                el = d[i - 1][w - weights[i - 1]] + costs[i - 1]
                d[i][w] = max(d[i - 1][w], el)

    if d[-1][-1] == 0:
        return [0, 0]
    res = list()
    res.append(d[-1][-1])

    indexes = list()
    i = n
    w = weight
    while d[i][w] != 0:
        if d[i][w] != d[i - 1][w]:
            indexes.append(i)
            w -= weights[i - 1]
            # compare i and w
        i -= 1

    # number of items K which allow to maximize total cost
    res.append(len(indexes))

    # indices of items which maximize total cost
    res.append(tuple(sorted(indexes)))

    return res


if __name__ == '__main__':
    ans = func(*read_cli('input.txt'))
    print(ans[0])
    print(ans[1])
    if len(ans) == 3:
        print(' '.join(map(str, ans[2])))

    ans = func(*read_cli('ex1.txt'))
    act = [15, 2, (2, 3)]
    assert ans == act

    ans = func(*read_cli('ex2.txt'))
    act = [30, 2, (1, 2)]
    assert ans == act

    ans = func(*read_cli('ex3.txt'))
    act = [0, 0]
    assert ans == act
