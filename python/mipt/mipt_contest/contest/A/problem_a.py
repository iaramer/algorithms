def get_trace(mat):
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                res += mat[i][j]
    return res


# if __name__ == '__main__':
#     import sys
#     sys.stdin = open('input001.txt', 'r')
#     inp = list()
#     for i in range(int(input())):
#         inp.append(tuple(map(int, input().split())))
#     assert get_trace(inp) == -137
#
#     sys.stdin = open('input002.txt', 'r')
#     inp = list()
#     for i in range(int(input())):
#         inp.append(tuple(map(int, input().split())))
#     assert get_trace(inp) == -63
#     print('GJ!')

inp = list()
for i in range(int(input())):
    inp.append(tuple(map(int, input().split())))
print(get_trace(inp))
