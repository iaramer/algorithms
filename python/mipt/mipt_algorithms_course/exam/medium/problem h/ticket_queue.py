"""
This problem is in "Normal" group

You decided to visit MIPT. You successfully arrived in Moscow and came to Savelovskiy railway station. Now you are
going to buy a ticket, but there are a lot of people who wants the same. They stand in a single huge queue.

Tickets are sold at K ticket windows, but the queue is common for all of these windows. When any window becomes free,
first person from the queue comes to this window, then he buys a ticket and leaves.

You have estimated amount of time (in seconds) each person will spend to buy a ticket (amount of time he will occupy
ticket window). When you came to station, all ticket windows were free (this mens, first K persons from the queue will
go to windows immediately).

You want to calculate number of seconds that will pass before all the persons in the queue will obtain their tickets.

Input format
First line contains two integer numbers: 0 < N ≤ 10^5, 0 < K ≤ 10^4 — number of persons in the queue and number of
ticket windows in the station.

Next line contains N integer numbers divided by space character: 0 < ti ≤ 10^5 — number of seconds i-th person will
occupy ticket window.

Output format
Print single integer number: number of seconds that will pass before all persons in the queue obtain their tickets.
"""

import heapq

DEBUG = True


def read_cli():
    N, K = map(int, input().split())
    t = map(int, input().split())
    return N, K, t


def func(pers, wins, ts):
    h = [0] * wins
    heapq.heapify(h)
    for ti in ts:
        tmp = heapq.heappop(h)
        heapq.heappush(h, tmp + ti)
    return max(h)


if __name__ == '__main__':
    if DEBUG:
        res = func(5, 2, [3, 1, 1, 2, 3])
        act = 6
        print(f'{res}, {act}')
        assert act == res

        res = func(7, 3, [1, 2, 3, 4, 5, 3, 1])
        act = 7
        print(f'{res}, {act}')
        assert act == res

        res = func(3, 100, [1, 2, 3])
        act = 3
        print(f'{res}, {act}')
        assert act == res
    else:
        print(func(*read_cli()))
