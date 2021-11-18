# def get_arr(n):
#     i0 = i1 = 1
#     res = [i0, i1]
#     if n >= 2:
#         for i in range(2, n+1):
#             summ = res[i-1] + res[i-2]
#             res.append(summ)
#     return res
#
#
# def fib(nums):
#     if not nums:
#         return 0
#     arr = get_arr(max(nums))
#     s = sum([arr[num] for num in nums])
#     return s % 4294967296


def get_arr2(nums):
    nums = sorted(nums)
    i0 = i1 = 1
    if i0 + i1 > nums[-1]:
        return len(nums)
    res = 0
    j = 0
    n = 2
    while j < len(nums) and n <= nums[-1]:
        if nums[j] == 0 or nums[j] == 1:
            res += 1
            j += 1
            continue
        if nums[j] > n:
            tmp = i0
            i0 = i1
            i1 += tmp
            n += 1
            continue
        res += i0 + i1
        j += 1
    return res


def fib(nums):
    if not nums:
        return 0
    ress = get_arr2(nums)
    return ress % 4294967296


# if __name__ == '__main__':
    # assert fib([]) == 0
    # assert fib([0]) == 1
    # assert fib([1]) == 1
    # assert fib([0, 1, 0, 1, 0]) == 5
    # assert fib([0, 1]) == 2
    # assert fib([0, 1, 2]) == 4
    # assert fib([2]) == 2
    #
    # import sys
    # sys.stdin = open('input001.txt', 'r')
    # inp = list()
    # for i in range(int(input())):
    #     inp.append(int(input()))
    # ans = fib(inp)
    # assert ans == 15
    # print('GJ!')

inp = list()
for i in range(int(input())):
    inp.append(int(input()))
print(fib(inp))
