def test_single_element(func):
    arr = [15]
    assert func(arr, 0, 1, 15) == 0


def test_min_element(func):
    nums = [i for i in range(10, 21, 2)]
    elem = 10
    assert func(nums, 0, len(nums)-1, elem) == nums.index(elem)


def test_max_element(func):
    nums = [i for i in range(10, 21, 2)]
    elem = 20
    assert func(nums, 0, len(nums)-1, elem) == nums.index(elem)


def test_out_of_bounds(func):
    nums = [i for i in range(10, 21, 2)]
    elem = 0
    assert func(nums, 0, len(nums)-1, elem) == -1
    elem = 100
    assert func(nums, 0, len(nums)-1, elem) == -1


def test_searching(func):
    test_single_element(func)
    test_min_element(func)
    test_max_element(func)
    test_out_of_bounds(func)
