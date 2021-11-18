"""
That traditional separation way isn't good enough. When there are 29 students in the class, usually no one notices why. But, for example, if heights of players are [195, 180, 170, 167, 150] it would be better to separate them into [195, 180] + [170, 167, 150] groups then [195, 170, 150] + [180, 167].

Think about how you can achieve the most honest separation if team sizes may differ by no more than 1 player?
"""


def sep(l):
    a = list()
    b = list()
    l.sort(reverse=True)


if __name__ == '__main__':
    inp = [195, 180, 170, 167, 150]
    ans = ([195, 180], [170, 167, 150])
    assert sep(inp) == ans

    print('OK')
