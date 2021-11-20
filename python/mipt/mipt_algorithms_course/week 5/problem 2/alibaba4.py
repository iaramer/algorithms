"""
Ali Baba decided to share golden bars he brought home in previous problem with you. Because you helped him a lot! He
used your fantastic programs to choose items in the cave!

Also, he wants to be honest, so, he wants to divide these  golden bars into two parts such that costs of these parts
are exactly equal.

Help him one more time. Write a program which will check if it's possible to divide bars with given costs ci into two
parts with identical total costs?

Input format
First line contains single integer number:  — number of golden bars.

Second line contains N integer numbers divided by space character  — costs of these items. It is guaranteed that sum of
costs of all items  is .

Output format
Print "YES" if it's possible to divide items into two parts with identical total costs. Print "NO" otherwise.
"""


def func_logic(costs):
    total = sum(costs)
    if total % 2 == 1:
        return False

    costs.sort()
    number = total // 2
    d = [[1] + [0] * number for _ in range(len(costs) + 1)]
    for i in range(1, len(costs) + 1):
        for w in range(1, number + 1):
            if costs[i - 1] > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = d[i - 1][w] or d[i - 1][w - costs[i - 1]]
    return bool(d[-1][number])


def func(costs):
    res = func_logic(costs)
    return 'YES' if res else 'NO'


if __name__ == '__main__':
    input()
    print(func(list(map(int, input().split()))))

    inp = [3, 2, 5]
    act = 'YES'
    assert func(inp) == act

    inp = [5, 4, 1, 0]
    act = 'YES'
    assert func(inp) == act

    inp = [7, 1, 5, 2]
    act = 'NO'
    assert func(inp) == act

    print('OK')
