"""
You are asked to implement QSort algorithm.

It already has input and output parts. Also it has qsort main function implemented.
You need to implement partition function which divides an array into 3 parts (p<, p=, p>).
This function should give you correct QSort algorithm.

Solution will be tested as sorting algorithm.

Input format
First line contains single integer number: 0 ≤ N ≤ 100000.
Next line contains N integer numbers divided by space character: 0 ≤ xi ≤ 109.

Output format
On single line you should print N integer numbers, divided by space character: xi in sorted (non-decreasing) order.

Input
3
0 2 1
Output
0 1 2

Input
3
800000000 1000000000 900000000
Output
800000000 900000000 1000000000
"""


def partition(x, l, r, pi):
    """
    :param x: Source array (list)
    :param l: left border of partitioning range (int)
    :param r: right border (not included) of partitioning range (int)
    :param pi: pivot element to divide array (any item from x[l, r)).
    :return: il, ir -- desired partition
    This function should reorder elements of x within [l, r) region
    in the way, these conditions are true:
    x[l:il] < pivot
    x[il:ir] == pivot
    x[ir:r] > pivot
    """
    i = l
    while i < r:
        el = x[i]
        j = i
        if el < x[pi]:
            while j >= pi:
                if j == pi:
                    pi += 1
                    break
                x[j], x[j - 1] = x[j - 1], x[j]
                j -= 1
        elif el > x[pi]:
            while j <= pi:
                if j == pi:
                    pi -= 1
                    i -= 1
                    break
                x[j], x[j + 1] = x[j + 1], x[j]
                j += 1
        i += 1
    return pi, pi + 1


# def qsort(x, l=0, r=None):
#     if r is None:
#         r = len(x)
#     if (r - l) > 1:
#         pivot_index = random.randint(l, r - 1)
#         il, ir = partition(x, l, r, pivot_index)
#         qsort(x, l, il)
#         qsort(x, ir, r)


def qsort(arr):
    if len(arr) <= 1:
        return arr
    pi = len(arr) // 2
    r = list()
    l = list()
    n = 0
    for i in range(len(arr)):
        if arr[i] == arr[pi]:
            n += 1
        if arr[i] > arr[pi]:
            r.append(arr[i])
        if arr[i] < arr[pi]:
            l.append(arr[i])
    return qsort(l) + [arr[pi]] * n + qsort(r)


if __name__ == '__main__':
    # N = int(input())
    # x = list(map(int, input().split()))
    # qsort(x)
    # print(' '.join(map(str, x)))

    inp = [1, 8, 4, 6, 2]
    exp = [1, 2, 4, 6, 8]
    inp = qsort(inp)
    assert inp == exp

    inp = [1, 7, 2, 1, 8, 4, 6, 2]
    exp = [1, 1, 2, 2, 4, 6, 7, 8]
    inp = qsort(inp)
    assert inp == exp

    print('it\'s ok!')
