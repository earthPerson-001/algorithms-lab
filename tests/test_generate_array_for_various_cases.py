import unittest

from setup_test import setup_paths  # to setup the paths and other related things

setup_paths()

from src.lab2.generate_array_for_various_cases import (
    generate_array_for_quick_sort_best_case,
    generate_array_for_merge_sort_worst_case,
)


class ArrayGenerationQuickSortBestCaseTest(unittest.TestCase):

    def test_quick_best_ten(self):
        arr = [94, 67, 15, 45, 27, 95, 89, 40, 54, 42]
        result = generate_array_for_quick_sort_best_case(arr)
        self.assertListEqual(result, [15, 42, 40, 27, 67, 54, 95, 94, 89, 45])

    def test_quick_best_five(self):
        arr = [1, 2, 3, 4, 5]
        result = generate_array_for_quick_sort_best_case(arr)
        self.assertListEqual(result, [2, 1, 5, 4, 3])

    def test_quick_best_seven(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        result = generate_array_for_quick_sort_best_case(arr)
        self.assertListEqual(result, [1, 3, 2, 5, 7, 6, 4])


class ArrayGenerationMergeSortWorstCase(unittest.TestCase):

    def test_merge_worst_ten(self):
        arr = [94, 67, 15, 45, 27, 95, 89, 40, 54, 42]
        result = generate_array_for_merge_sort_worst_case(arr)
        self.assertListEqual(result, [94, 15, 45, 67, 40, 95, 27, 54, 89, 42])

    def test_sorted_16(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        result = generate_array_for_merge_sort_worst_case(arr)
        self.assertListEqual(
            result, [9, 1, 13, 5, 11, 3, 15, 7, 10, 2, 14, 6, 12, 4, 16, 8]
        )

    def test_sorted_7(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        result = generate_array_for_merge_sort_worst_case(arr)
        self.assertListEqual(result, [4, 0, 6, 2, 5, 1, 7, 3])

    def test_sorted_8(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        result = generate_array_for_merge_sort_worst_case(arr)
        self.assertListEqual(result, [8, 0, 4, 6, 2, 5, 1, 7, 3])


if __name__ == "__main__":
    unittest.main()
