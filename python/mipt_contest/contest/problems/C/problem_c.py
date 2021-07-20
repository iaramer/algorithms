from collections import Counter


def poly(s):
    res = list()
    d = dict(Counter(s).most_common())
    l = lambda item: item[1]>1
    dd = dict(filter(l, d.items()))
    for c in sorted(dd, key=lambda it: it[0]):
        res += [c] * (dd[c] // 2)

    d1 = dict(filter(lambda item: item[1]==1, d.items()))
    sin = sorted(list(d1.keys()))[0]
    res = res + [sin] + res[::-1]
    return ''.join(res)


# if __name__ == '__main__':
#     import sys
#     sys.stdin = open('input001.txt', 'r')
#     assert poly(input()) == 'k'
#
#     sys.stdin = open('input002.txt', 'r')
#     assert poly(input()) == 'iai'
#     print('GJ!')

print(poly(input()))
