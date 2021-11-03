"""
Algorithms and data structures course is over. All exams have passed, and MSAI teachers are going to analyse the result. The number of students in MSAI program this year was 3 ≤ N ≤ 1000. Teachers have an excel table with the following information about each student:

unique student id;
student score for the course;
Student nickname.
Unfortunately, teachers don't know how to sort tables in excel, and they decided to ask you to write program to do that.

You need to provide students ids in non-increasing score order. If two students have identical score, one who have less id should go first (see Sample 3).

Also, teachers want your program to print nicknames of three students who took 1st, 2nd and 3rd place in sorted table to give them a prize.

Input format
First line contains single integer number: 3 ≤ N ≤ 1000. The following N lines contain information about students. i-th line contains the following:

Integer number 0 ≤ id < N (unique student id);
Space character;
Integer number 0 ≤ score ≤ 109 (student score for the course);
Space character;
String which consists of 1-20 latin letters (A-Z, a-z): (student nickname).
Line break character ;
Output format
First three lines should contain nicknames of 3 prize-winners (students who took 1st, 2nd and 3rd place in sorted table). Fourth line should contain N integer numbers divided by space character — ids of students in non-increasing score order. If two students have identical score, one who have less id should go first (see Sample 3).

Sample 1
Input
5
0 100 Kermit
1 0 Pepe
2 999999999 Knuth
3 1000000000 Dijkstra
4 100000000 Kormen
Output
Dijkstra
Knuth
Kormen
3 2 4 0 1

Sample 2
Input
4
3 10 McDonald
1 50 Ivan
0 1000 AdaLovelace
2 100 Radoslav
Output
AdaLovelace
Radoslav
Ivan
0 2 1 3
Sample 3
Input
3
2 1 a
1 1 b
0 1 c
Output
c
b
a
0 1 2

Notes
Please, use any Quadratic sorting algorithm covered in lecture in this problem solution.
"""


def selection_sort(arr):
    fs = 0
    while fs < len(arr):
        me, mi = arr[fs], fs
        for i in range(fs + 1, len(arr)):
            if arr[i][0] > me[0]:
                me = arr[i]
                mi = i
            elif arr[i][0] == me[0] and arr[i][1] < me[1]:
                me = arr[i]
                mi = i
        if mi != fs:
            del arr[mi]
            arr.insert(fs, me)
        fs += 1
    return arr


# inp = list()
# for i in range(int(input())):
#     idx, score, name = input().split()
#     idx, score = int(idx), int(score)
#     inp.append((score, idx, name))

# l = selection_sort(inp)

# for i in range(min(3, len(inp))):
#     print(l[i][2])
# print(' '.join([str(x[1]) for x in l]))

if __name__ == '__main__':
    import sys
    sys.stdin = open('ex1.txt', 'r')

    inp = list()
    for i in range(int(input())):
        idx, score, name = input().split()
        idx, score = int(idx), int(score)
        inp.append((score, idx, name))

    l = selection_sort(inp)

    for i in range(min(3, len(inp))):
        print(l[i][2])
    print(' '.join([str(x[1]) for x in l]))
