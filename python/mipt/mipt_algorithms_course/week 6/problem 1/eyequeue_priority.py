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


def read_cli(file):  # TODO: rewrite
    inputs = list()
    n_shops = None
    for line in open(file, 'r'):
        cmd = line.split()
        if len(cmd) == 1:
            if cmd[0].isdigit():
                n_shops = int(cmd[0])
            else:
                break
        elif len(cmd) == 2:
            inputs.append((cmd[0], int(cmd[1])))
        elif len(cmd) == 3:
            inputs.append((cmd[0], int(cmd[1]), int(cmd[2])))
    return inputs, n_shops


def func():
    pass


if __name__ == '__main__':
    res = func(*read_cli('ex1.txt'))
    act = [0, 2, 1]
    assert res == act

    res = func(*read_cli('ex2.txt'))
    act = [0, 3, 4, 1, 2]
    assert res == act

    res = func(*read_cli('ex3.txt'))
    act = [3, 4, 5, 0, 1, 2]
    assert res == act
