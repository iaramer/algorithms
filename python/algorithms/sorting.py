import random


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    i = j = k = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        k += 1

    while i < len(left):
        res.append(left[i])
        i += 1
        k += 1

    while j < len(right):
        res.append(right[j])
        j += 1
        k += 1

    return res


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    are_equal = True

    for i in range(1, len(nums)):
        if nums[i] != nums[0]:
            are_equal = False
    if are_equal:
        return nums

    pivot = random.choice(nums)
    left = []
    right = []
    for num in nums:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + quick_sort(right)
