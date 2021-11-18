"""
Даны два отрезка. Требуется выяснить, не пересекаются ли они.
Входные данные содержат восемь чисел, не превосходящих по модулю 104 — координаты концов двух отрезков.
Выведите “YES”, если отрезки имеют общие точки, и “NO” в противном случае.
"""


def check_intersection(vec1, vec2) -> str:
    res = False
    x1, y1, x2, y2 = vec1
    x3, y3, x4, y4 = vec2
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0:
        return 'NO'
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d
    res = (min(x1, x2) <= px <= max(x1, x2)) and (min(x3, x4) <= px <= max(x3, x4)) and \
          (min(y1, y2) <= py <= max(y1, y2)) and (min(y3, y4) <= py <= max(y3, y4))
    return 'YES' if res else 'NO'


if __name__ == '__main__':
    v1 = [0, 0, 10, 10]  # [x1, y1, x2, y2]
    v2 = [0, 10, 10, 0]  # [x3, y3, x4, y4]
    test = check_intersection(v1, v2)
    assert test == 'YES'

    v1 = [0, 10, 10, 0]  # [x1, y1, x2, y2]
    v2 = [0, 9, 9, 0]  # [x3, y3, x4, y4]
    test = check_intersection(v1, v2)
    assert test == 'NO'

    v1 = [0, 0, 4, 4]  # [x1, y1, x2, y2]
    v2 = [0, 10, 10, 0]  # [x3, y3, x4, y4]
    test = check_intersection(v1, v2)
    assert test == 'NO'
    print('It\'s ok!')
