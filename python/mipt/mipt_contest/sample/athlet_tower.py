"""
В город N приехал цирк с командой атлетов. Они хотят удивить горожан города N — выстроить из своих тел башню
максимальной высоты. Башня — это цепочка атлетов, первый стоит на земле, второй стоит у него на плечах, третий стоит на
плечах у второго и т.д.
Каждый атлет характеризуется силой si (in kg) и массой mi (in kg). Сила — это максимальная масса, которую атлет
способен держать у себя на плечах.
К сожалению, ни один из атлетов не умеет программировать, так как всю жизнь они занимались физической подготовкой и у
них не было времени на изучение языков программирования. Помогите им, напишите программу, которая определит
максимальную высоту башни, которую они могут составить.
Вход Первая строчка входа содержит число n атлетов, а далее следуют n строчек с их параметрами:

n
m1 s1
m2 s2
...
mn sn

Известно, что если атлет тяжелее, то он и сильнее:
если mi>mj, то si > sj.
Но атлеты равной массы могут иметь различную силу.
Число атлетов 1 ≤ n ≤ 100000. Масса и сила являются положительными целыми числами меньше, чем 2000000.
Выход должен содержать натуральное число — максимальную высоту башни.
Вход#1
4
3 4
2 2
7 6
4 5
Выход#1
3
"""


def calc_tower(inp):
    aths = sorted([(int(a[0]), int(a[1])) for a in inp[1:]], key=lambda a: a[0])  # sort by mass asc
    res = 0
    sum_mass = 0
    while aths:
        if max(aths, key=lambda a: a[1])[1] < sum_mass:
            break
        for ath in aths:
            if ath[1] >= sum_mass:
                res += 1
                sum_mass += ath[0]
                aths.remove(ath)
                break
    return res


if __name__ == '__main__':
    data = [
        4,
        ('3', '4'),
        ('2', '2'),
        ('7', '6'),
        ('4', '5')
    ]
    ans = str(calc_tower(data))
    assert ans == '3'
    print('GJ!')
