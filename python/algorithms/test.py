from algorithms.general_test import test_sorting_algorithm
from algorithms.sorting import merge_sort, quick_sort


def test_merge_sort():
    test_sorting_algorithm(merge_sort)


def test_quick_sort():
    test_sorting_algorithm(quick_sort)
