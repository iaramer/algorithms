"""
Pear company is preparing for presenting their new device called EyeWatch. This time they decided to change the rules
of queuing customers. New rules are much easier:

Customers may purchase special priority certificates before start of sales. The cost of certificate is not fixed —
customers are free to pay any amount of money they want. This certificate gives the customer a "priority" that is
numerically equal to amount of money he payed for the certificate.

In the queue the next customer who should enter the shop is the one with largest priority among all people currently
present in the queue, if there are several customers with such priority — one who came first is chosen.

Customers without certificates are considered to have priority 0.

Company is now just testing their idea, so, this system will be tested in only one store. Write a program which will
simulate the queueing process in one store.

Input format
The first line of input file contains the only integer number: 0 ≤ N ≤ 100000 – the number of events your program
should process.

The following 0 ≤ N ≤ 100000 lines contain events your program need to process.

The line defining i-th event starts with symbol + or - which denotes type of event. + means that new customer entered
the queue. - means that next customer with maximum priority (among all with equal priority — one who entered the queue
first) enters the shop. Then, for + event goes two integer numbers divided by space character : 0 ≤ idi < N,
0 ≤ pi < 109 — id (just number of customer, starting from 0) and priority of i-th customer.

Output format
For each event of type - print id of customer who enters the shop during this event on separate line.
"""


import math


def sift_up(data, i):
    if i == 0:
        return
    parent = (i - 1) // 2
    if data[parent] > data[i]:
        data[parent], data[i] = data[i], data[parent]
        sift_up(data, parent)


def sift_down(data, i):
    child1 = i * 2 + 1
    child2 = i * 2 + 2
    if child1 >= len(data):
        return
    if child2 >= len(data):
        child_min = child1
    else:
        child_min = child1 if data[child1] < data[child2] else child2
    if data[child_min] < data[i]:
        data[i], data[child_min] = data[child_min], data[i]
        sift_down(data, child_min)


def heapify(data):
    for i in range(len(data) - 1, -1, -1):
        sift_down(data, i)


def heappush(data, x):
    data.append(x)
    sift_up(data, len(data) - 1)


def heappop(data, i=0):
    data[i], data[-1] = data[-1], data[i]
    res = data.pop()
    sift_up(data, i)
    sift_down(data, i)
    return res


def read_cli(file):
    inputs = list()
    for line in open(file, 'r'):
        cmd = line.split()
        if len(cmd) == 1:
            inputs.append('-')
        else:
            priority = math.inf
            if len(cmd) == 3 and cmd[2] != '0':
                priority = 1 / int(cmd[2])
            inputs.append((int(cmd[1]), priority))
    return inputs[1:]


def func(arr):
    res = []
    h = []
    for el in arr:
        if el == '-':
            res.append(heappop(h)[1])
        else:
            heappush(h, (el[1], el[0]))
    return res


if __name__ == '__main__':
    # for n in func(read_cli('input.txt')):
    #     print(n)

    res = func(read_cli('ex1.txt'))
    act = [0, 2, 1]
    assert res == act

    res = func(read_cli('ex2.txt'))
    act = [0, 3, 4, 1, 2]
    assert res == act

    res = func(read_cli('ex3.txt'))
    act = [3, 4, 5, 0, 1, 2]
    assert res == act

    print('OK!')
