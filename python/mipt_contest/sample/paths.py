"""
Из верхнего левого угла в правый нижний угол сетки 2x2 можно пройти 6 разными путями
(без возвратов, т.е. если идти только вниз или вправо). Сколько таких разных путей можно найти в сетке N×M?
Входные данные
Целые числа 1 ≤ N, M ≤ 20 через пробел.
Выходные данные
Количество разных путей.

Примеры
Вход/Input
2 2
Выход/Output
6
"""


def calc_paths(n, m):
    cell = []
    for i in range(m+1):
        row = []
        if i == 0:
            row = [1] * (n+1)
            row[0] = 2
        else:
            row = [1] * (n+1)
            for j in range(1, n+1):
                up = cell[max(i-1, 0)][j]
                left = row[max(j-1, 0)]
                row[j] = up+left
        cell.append(row)
    return cell[-1][-1]


if __name__ == '__main__':
    # a, b = list(map(int, input().split()))
    # print(calc_paths(a, b))

    assert calc_paths(1, 1) == 2
    assert calc_paths(1, 2) == 3
    assert calc_paths(1, 3) == 4
    assert calc_paths(3, 1) == 4
    assert calc_paths(2, 2) == 6
    assert calc_paths(2, 3) == 10
    assert calc_paths(3, 3) == 20
    print('GJ!')
