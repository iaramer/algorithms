def test_empty(func):
    assert func([]) == []


def test_single_element(func):
    assert func([1]) == [1]


def test_equal_elements(func):
    nums = [1, 1, 1, 1]
    res = [1, 1, 1, 1]
    assert func(nums) == res


def test_asc_elements_no_repeats(func):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert func(nums) == res


def test_asc_elements_with_repeats(func):
    nums = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10]
    res = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10]
    assert func(nums) == res


def test_desc_elements_no_repeats(func):
    nums = [7, 6, 5, 4, 3, 2, 1]
    res = [1, 2, 3, 4, 5, 6, 7]
    assert func(nums) == res


def test_desc_elements_with_repeats(func):
    nums = [7, 6, 6, 5, 4, 4, 4, 3, 2, 1, 1, 1]
    res = [1, 1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 7]
    assert func(nums) == res


def test_chaotic_elements_no_repeats(func):
    nums = [6, 2, 7, 5, 1, 4, 3]
    res = [1, 2, 3, 4, 5, 6, 7]
    assert func(nums) == res


def test_chaotic_elements_with_repeats(func):
    nums = [6, 2, 1, 6, 7, 5, 1, 5, 6, 4, 1, 3]
    res = [1, 1, 1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
    assert func(nums) == res
