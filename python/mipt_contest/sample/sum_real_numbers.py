"""
Сложите положительные действительные числа, пришедшие на стандартный вход
Чисел не более 10^7. Точность не менее 10^-20
Стиль кода
Пример входа
1.2 3.4 5.6
Пример выхода
10.2
"""


def sum_nums(num1, num2):
    res = ''
    f1 = -(len(num1) - num1.index('.'))
    f2 = -(len(num2) - num2.index('.'))
    if f2 < f1:
        num1, num2 = num2, num1
        f1, f2 = f2, f1

    diff = f1 - f2
    if diff < 0:
        res += num1[diff:]
        num1 = num1[:diff]

    num1 = num1.replace('.', '')
    num2 = num2.replace('.', '')

    res = str(int(num1) + int(num2)) + res
    res = res[:f1+1] + '.' + res[f1+1:]
    return res


def sum_real_nums(nums):
    res = '0.0'
    for num in nums:
        if '.' not in num:
            num += '.0'
        res = sum_nums(res, num)
    return res


if __name__ == '__main__':
    test_list = ['3.000000000000000000000000000000003', '3.000000000000000000000000000000003',
                 '3.000000000000000000000000000000003', '3.000000000000000000000000000000003']
    answer = '12.000000000000000000000000000000012'
    assert sum_real_nums(test_list) == answer
    test_list = ['3.300000000000000000000000000000003', '3.300000000000000000000000000000003',
                 '3.300000000000000000000000000000003', '3.300000000000000000000000000000003']
    answer = '13.200000000000000000000000000000012'
    assert sum_real_nums(test_list) == answer
    test_list = ['300000000000000000000000000000003.0', '0.300000000000000000000000000000003']
    answer = '300000000000000000000000000000003.300000000000000000000000000000003'
    assert sum_real_nums(test_list) == answer
    test_list = ['6', '6.300000000000000000000000000000003']
    answer = '12.300000000000000000000000000000003'
    assert sum_real_nums(test_list) == answer
    test_list = ['6.6', '606.606']
    answer = '613.206'
    assert sum_real_nums(test_list) == answer
    test_list = ['5.5', '5.5']
    answer = '11.0'
    assert sum_real_nums(test_list) == answer

    print('it\'s ok!')
