"""
Implement deque data structure. This data structure was not covered in the lecture, but it's quite easy.
Deque is also called double-ended queue (Double-Ended QUEue). This is a data structure, defined by functionality,
and it should support the following operations:

push_back;
push_front;
len;
pop_back;
pop_front.

You are given list of 1 ≤ N ≤ 100000 requests to deque data structure. You need to process these requests,
and check for possible errors (pop from empty dequeue). If the request cannot be processed, it should not make any
changes in deque.

Request types are encoded by integer numbers:

0 — push_back;
1 — push_front;
2 — len;
3 — pop_back;
4 — pop_front;
-1 — End of list.

Input format
Each line contains a request description, which consists of 1 or 2 integer numbers.

First number is a request type. For request types 0, 1, line also contains space character followed by one more
integer number: value to be pushed to deque: 0 ≤ v ≤ 109.

Last line of input file contains one integer number: -1, which denotes end of list of requests.

Total number of requests do not exceed 100000.

Output format
For each request of types 2-4, write a result on a separate line (requested length, or value to be removed by pop).
If request cannot be performed, you should write Error! on separate line.



Notes
Please, notice that all mentioned deque operations should have O(1) complexity to meet time limit in this task.

Python has collections.deque data structure built in. Please, don't use it in this problem.
But you can use it to test your own deque.
"""

import sys


def read_cli(file):
    sys.stdin = open(file, 'r')
    commands = list()
    command = tuple(map(int, input().split()))
    while command[0] != -1:
        commands.append(command)
        command = tuple(map(int, input().split()))
    return commands


def perform(commands):
    deq = AIDequeue()
    res = list()
    for command in commands:
        if command[0] == 0:
            deq.push_back(command[1])
        elif command[0] == 1:
            deq.push_front(command[1])
        elif command[0] == 2:
            res.append(len(deq))
        elif command[0] == 3:
            res.append(deq.pop_back())
        elif command[0] == 4:
            res.append(deq.pop_front())
    return res


class AIDequeue:
    def __init__(self, init_len=100):
        self.length = 0
        self.array = [None] * init_len
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        return self.length

    def len(self) -> int:
        return self.length

    def push_back(self, element) -> None:
        if self.length == 0:
            self.head = self.tail = 0
        else:
            if self.tail + 1 < len(self.array):  # don't need to do a circle
                if self.tail + 1 == self.head:
                    self.array = self.array[:self.head] \
                        + [None] * len(self.array) \
                        + self.array[self.head:]  # O(N)
                    self.head += len(self.array) // 2
                self.tail += 1
            else:  # need to do a circle
                if 0 == self.head:
                    self.array = [None] * len(self.array) + self.array  # O(N)
                    self.head += len(self.array) // 2
                self.tail = 0
        self.array[self.tail] = element
        self.length += 1

    def push_front(self, element) -> None:
        if self.length == 0:
            self.head = self.tail = 0
        else:
            if self.head - 1 >= 0:  # don't need to do a circle
                if self.head - 1 == self.tail:
                    self.array = self.array[:self.head] \
                        + [None] * len(self.array) \
                        + self.array[self.head:]  # O(N)
                    self.head += len(self.array) // 2
                self.head -= 1
            else:  # need to do a circle
                if len(self.array) - 1 == self.tail:
                    self.array += [None] * len(self.array)  # O(N)
                self.head = len(self.array) - 1
        self.array[self.head] = element
        self.length += 1

    def pop_back(self):
        if self.length == 0:
            return 'Error!'
        el = self.array[self.tail]
        if self.tail == 0:
            self.tail = len(self.array) - 1
        else:
            self.tail -= 1
        self.length -= 1
        return el

    def pop_front(self):
        if self.length == 0:
            return 'Error!'
        el = self.array[self.head]
        if self.head == len(self.array) - 1:
            self.head = 0
        else:
            self.head += 1
        self.length -= 1
        return el


if __name__ == '__main__':
    act = [3, 2, 4, 2, 7]
    res = perform(read_cli('ex1.txt'))
    assert res == act

    act = [2, 3, 8, 4]
    res = perform(read_cli('ex2.txt'))
    assert res == act

    act = ['Error!', 6, 8, 4, 7, 2, 9, 'Error!']
    res = perform(read_cli('ex3.txt'))
    assert res == act

    print('OK')
