from collections import Counter


def poly(s):
    res = ''
    dd = dict()
    sin = ''
    for k, v in Counter(s).most_common():
        if v > 1:
            dd[k] = v
        elif v == 1 and (sin == '' or k < sin):
                sin = k

    for c in sorted(dd.keys()):
        res += c * (dd[c] // 2)
        if dd[c] % 2 == 1 and (sin == '' or c < sin):
            sin = c

    res = res + sin + res[::-1]
    return res


# if __name__ == '__main__':
#     import sys
#     sys.stdin = open('input001.txt', 'r')
#     assert poly(input()) == 'k'
#
#     sys.stdin = open('input002.txt', 'r')
#     assert poly(input()) == 'iai'
#
#     assert poly('jijijijijijijijijijij') == 'iiiiijjjjjjjjjjjiiiii'
#     print('GJ!')

print(poly(input()))
