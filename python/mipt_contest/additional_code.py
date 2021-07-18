"""
Дополнительный код
Дано целое число А. Выведите запись числа A в двоичном 8-разрядном дополнительном коде.
Ограничения: -128 ≤ A ≤ 127.
"""


def additional_code(num):
    if num > 0:
        res = f'{num:08b}'
    else:
        d = {'0': '1', '1': '0'}
        num += 1
        res = '1' + ''.join([d[i] for i in f'{-num:07b}'])
    return res


arg = int(input())
result = additional_code(arg)
print(result)
