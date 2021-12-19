"""
Covid-19 pandemic is finally over! State borders open again and airlines return to work. You want to visit MIPT,
because you need to get your student id. Also you want to see sights of Dolgoprudny.

You have K days to take student ID, because you are going to use it to get discount in K days. So, you need to get
from your home city to Moscow not later than in K days. Also, you decided that you don't want to have more than one
flight per day, because it's too hard. So, this means, you can't have more than K flights in your path.

Also, you want to minimize total cost of your flights. You have obtained schedules of flights (list of flights is the
same every day). Now you just need to implement an algorithm which will choose the best path for you.

Input format
The first line contains 4 integer numbers: 2 ≤ N ≤ 100; 0 ≤ s, f < N; 0 ≤ K < N — number of cities in the schedule, id
of your home city (s) and id of Moscow airport (f), and K — maximum number of flights you can make.

Next N lines contain N integer numbers each and define matrix a (adjacency matrix of the graph).
Value ai, j in i-th row j-th column is the cost of flight from city i to city j. If there's no flights from i to j,
this value equals -1: -1 ≤ ai, j ≤ 10000. It is guaranteed that a contains only -1 values on main diagonal.

Output format
Print single integer number — minimum cost of the path  which contains not more than K flights. If path satisfying
given conditions doesn't exist, print -1.
"""


def func():
    pass


if __name__ == '__main__':
    res = func()
    act = 30
    assert res == act

    res = func()
    act = 200
    assert res == act

    res = func()
    act = 1000
    assert res == act

    res = func()
    act = 4
    assert res == act
