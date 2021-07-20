def p_on_line(px, py, x1, y1, x2, y2):
    if (x1==px and y1 == py) or (x2==px and y2 == py):
        return True
    if x2 - x1 == 0:
        if px == x1 and ((y1 <= py <= y2) or (y2 <= py <= y1)):
            return True
        else:
            return False
    slope = (y2 - y1) / (x2 - x1)
    p_on = (py - y1) == slope * (px - x1)
    p_between = (min(x1, x2) <= px <= max(x1, x2)) and (min(y1, y2) <= py <= max(y1, y2))
    return p_on and p_between


def check_intersection(vec1, vec2) -> int:
    x1, y1, x2, y2 = vec1
    x3, y3, x4, y4 = vec2

    # not segment but point
    if (x1 == x2) and (y1 == y2):
        int(p_on_line(x1, y1, x3, y3, x4, y4))
    elif (x3 == x4) and (y3 == y4):
        int(p_on_line(x3, y3, x1, y1, x2, y2))

    # det
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0:
        return int(p_on_line(x1, y1, x3, y3, x4, y4)) or int(p_on_line(x2, y2, x3, y3, x4, y4)) or \
               int(p_on_line(x3, y3, x1, y1, x2, y2)) or int(p_on_line(x4, y4, x1, y1, x2, y2))

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d

    res = (min(x1, x2) <= px <= max(x1, x2)) and (min(x3, x4) <= px <= max(x3, x4)) and \
          (min(y1, y2) <= py <= max(y1, y2)) and (min(y3, y4) <= py <= max(y3, y4))
    return int(res)


# if __name__ == '__main__':
#     v1 = [0, 0, 10, 10]  # [x1, y1, x2, y2]
#     v2 = [0, 10, 10, 0]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [0, 10, 10, 0]  # [x1, y1, x2, y2]
#     v2 = [0, 9, 9, 0]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 0
#
#     v1 = [0, 0, 4, 4]  # [x1, y1, x2, y2]
#     v2 = [0, 10, 10, 0]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 0
#
#     v1 = [2, 0, 2, 2]  # [x1, y1, x2, y2]
#     v2 = [0, 1, 7, 1]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [2, 0, 2, 0]  # [x1, y1, x2, y2]
#     v2 = [2, 0, 2, 1]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [2, 0, 2, 1]  # [x1, y1, x2, y2]
#     v2 = [1, 0, 1, 1]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 0
#
#     v1 = [0, 1, 2, 1]  # [x1, y1, x2, y2]
#     v2 = [1, 0, 1, 2]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [0, 0, 2, 2]  # [x1, y1, x2, y2]
#     v2 = [2, 2, 0, 2]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [0, 0, 10, 10]  # [x1, y1, x2, y2]
#     v2 = [2, 2, 8, 8]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [0, 0, 4, 4]  # [x1, y1, x2, y2]
#     v2 = [2, 2, 8, 8]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [0, 0, 0, 0]  # [x1, y1, x2, y2]
#     v2 = [0, 0, 0, 0]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     v1 = [0, 0, 0, 0]  # [x1, y1, x2, y2]
#     v2 = [1, 1, 1, 1]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 0
#
#     v1 = [0, 0, 0, 2]  # [x1, y1, x2, y2]
#     v2 = [0, 1, 0, 1]  # [x3, y3, x4, y4]
#     test = check_intersection(v1, v2)
#     assert test == 1
#
#     print('It\'s ok!')

v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
print(check_intersection(v1, v2))
