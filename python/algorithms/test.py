from test_sorting import *
from sorting import *


def algorithm_test(func):
    test_empty(func)
    test_single_element(func)
    test_equal_elements(func)
    test_asc_elements_no_repeats(func)
    test_asc_elements_with_repeats(func)
    test_desc_elements_no_repeats(func)
    test_desc_elements_with_repeats(func)
    test_chaotic_elements_no_repeats(func)
    test_chaotic_elements_with_repeats(func)


def test_merge_sort():
    algorithm_test(merge_sort)


def test_quick_sort():
    algorithm_test(quick_sort)


def test_insertion_sort_1():
    algorithm_test(insertion_sort_1)


def test_insertion_sort_2():
    algorithm_test(insertion_sort_2)
