"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflects the given points.

Example 1:
Given points = [[1,1],[-1,1]], return true.
Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?
"""

'''
for any point: E x=-(x'+k) & y=y'
x=k/2, y=any

Group points with equal y

[[3,1],[-1,1],[1,-5]]

d = {
        1: [3,-1]  # (-1+3)/2=1
        2: [-3,-2,3,4]  # (-3-2+3+4)/4 = 0.5
        3: [1,2,3]  # (1+2+3)/3 = 6
        -5: [1]
    }
    
d2 = {
    1: [0,2,4]  # 2
    2: [-1,0,2,4,5]  # 10/5=2
}
Если будет две точки по одним координатам - они сольются или считаются за 2 разные точки? 
Будем считать, что разные -> list() | Иначе: set()
'''


def check_points(arr):
    d = dict()
    for p in arr:
        if p[1] not in d.keys():
            d[p[1]] = list()
        d[p[1]].append(p[0])
    s = set()
    for v in d.values():
        s.add(sum(v) / len(v))
    return len(s) == 1


if __name__ == '__main__':
    p = [[1, 1], [-1, 1]]
    assert check_points(p) is True
    p = [[1, 1], [-1, -1]]
    assert check_points(p) is False
    p = [[1, 1], [-1, 1], [0, 3]]
    assert check_points(p) is True
    p = [[1, 1], [-1, -1], [0, 3]]
    assert check_points(p) is False
    p = [[1, -1], [1, 1]]
    assert check_points(p) is True
    p = [[1, 1], [3, 2], [-1, 1], [-3, 2]]
    assert check_points(p) is True
    p = [[1, 1], [3, 2], [-1, 1], [0, -5], [-3, 2]]
    assert check_points(p) is True
    p = [[0, 1], [2, 2], [-2, 1], [-1, -5], [-4, 2]]
    assert check_points(p) is True
    print('GJ!')
