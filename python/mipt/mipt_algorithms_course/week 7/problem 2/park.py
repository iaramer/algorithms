"""
You're in a hurry, because webinar on Algorithms and Data structures is about to start. On your way home there is a
park and you decided to go this park through. And you want to find the shortest way from the enter
(your current position) to the exit.

Fortunately, you've found a map of the park. This may help.

Map of the park is square array of the following characters:

. – empty space (you can go through it)

# – barrier, e.g. a tree (you can't go through it)

E – your current position (Enter)

X – your destination (eXit)

From position (i, j) you can move to one of the (i - 1, j), (i, j - 1), (i + 1, j) or (i, j + 1) only if there's no
barrier in target position.

Input format
The first line contains two integer numbers: 0 < N ≤ 500, 0 < M ≤ 500 — number of rows and columns in the map
respectively.

Each of the next N lines contains M characters each (terminated with line break character) and denote a map of the park.

It is guaranteed that there are exactly one E and exactly one X characters in the map.

Output format
Print one integer number — minimum number of steps you need to get from the current position to the exit. If it is
impossible, print -1.
"""


if __name__ == '__main__':
    # smth
