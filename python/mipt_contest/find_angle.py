"""
Даны два вектора. Найдите полярный угол между ними.
Входные данные содержат четыре целых числа, по модулю не превосходящих 10^4 координаты двух ненулевых векторов.
Выведите величину неориентированного угла между векторами из интервала [0, π] с абсолютной погрешностью не хуже 10^−5 .
"""
import numpy as np
import math


def find_angle(x1, y1, x2, y2):
    dot = np.dot([x1, y1], [x2, y2])
    sc = np.sqrt(x1**2 + y1**2) * np.sqrt(x2**2 + y2**2)
    cos = dot / sc
    cos = 1 if cos > 1 else cos
    cos = -1 if cos < -1 else cos
    return np.arccos(cos) * 180 / math.pi


if __name__ == '__main__':

    a1, b1, a2, b2 = 50, 55, 30, -17
    test = find_angle(a1, b1, a2, b2)
    print(test)
    assert round(test, 6) == 77.265093

    a1, b1, a2, b2 = 25, -30, -25, 30
    test = find_angle(a1, b1, a2, b2)
    print(test)
    assert round(test, 6) == 180

    print('It\'s ok!')
