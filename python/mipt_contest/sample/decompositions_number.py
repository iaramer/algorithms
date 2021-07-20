"""
Напишите программу, которая считает количество разложений P(N) данного натурального числа N на неупорядоченные
натуральные слагаемые. Например, для N = 5 есть 7 различных разложений:
5 = 4+1 = 3+2 = 3+1+1 = 2+2+1 = 2+1+1+1 = 1+1+1+1+1.
Разложения считаются различными если множества слагаемых различаются.
Формат ввода
Натуральное число N, 0 < N ≤ 100.
Формат вывода
Число P(N).
Sample input Sample output
5 7
15 176
"""


def count_dec(n):
    o = set()
    decs = [[n]]
    while decs:
        curr_dec = decs.pop()
        o.add(tuple(curr_dec))
        if set(curr_dec) == {1}:
            continue
        for d in curr_dec:
            if d != 1:
                cdec = curr_dec.copy()
                cdec.remove(d)
                decs.append(sorted(cdec + [d-1, 1]))
    return len(o)


if __name__ == "__main__":
    assert count_dec(5) == 7
    assert count_dec(15) == 176
