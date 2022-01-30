"""
This problem is in "Very simple" group

Exam session is a difficult time for everybody. Your friend (not you, of course) has problems with preparing to the
next exam: he knows nothing and has only M minutes left before the exam. He has list of questions for the exam and for
each question he has estimation of number of hours he need to study materials related to this question.

On the exam he will be given one question from this list. If he have been studied materials for the given question — he
will pass the exam, otherwise he will fail.

Help your friend to maximise probability of passing the exam. Write a program that will calculate maximum number of
questions your friend will manage to study materials for before the exam.

Input format
First line of input file contains two integer numbers: 0 < N ≤ 100000, 0 < M ≤ 109 — number of questions in the list
and number of minutes left before the exam.

Second line contains N integer numbers separated by space characters: 0 ≤ mi ≤ 104 — number of minutes needed to study
materials for question number i.

Output format
Print single integer number — maximum number of questions your friend will manage to study materials for before the
exam.
"""

DEBUG = False


def func(m, qs):
    res = 0
    qs.sort()
    for q in qs:
        if m - q < 0:
            break
        m -= q
        res += 1
    return res


if __name__ == '__main__':
    if DEBUG:
        pass
    else:
        n, m = map(int, input().split())
        qs = list(map(int, input().split()))
        print(func(m, qs))
