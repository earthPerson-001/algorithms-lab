import unittest

from setup_test import setup_paths  # to setup the paths and other related things

setup_paths()

from src.lab1.insertion_sort import insertion_sort
from src.lab1.selection_sort import selection_sort
from src.lab1.merge_sort import merge_sort


class InsertionSortTest(unittest.TestCase):

    def test_insertion_five(self):
        arr = [2, 3, 1, 0, 5]
        result = insertion_sort(arr)
        self.assertListEqual(result, [0, 1, 2, 3, 5])

    def test_insertion_empty(self):
        arr = []
        result = insertion_sort(arr)
        self.assertListEqual(result, [])

    def test_insertion_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = insertion_sort(arr)
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    def test_insertion_negative(self):
        arr = [-2, -3, -1, 0, -5]
        result = insertion_sort(arr)
        self.assertListEqual(result, [-5, -3, -2, -1, 0])


class SelectionSortTest(unittest.TestCase):

    def test_selection_five(self):
        arr = [2, 3, 1, 0, 5]
        result = selection_sort(arr)
        self.assertListEqual(result, [0, 1, 2, 3, 5])

    def test_selection_empty(self):
        arr = []
        result = selection_sort(arr)
        self.assertListEqual(result, [])

    def test_selection_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = selection_sort(arr)
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    def test_selection_negative(self):
        arr = [-2, -3, -1, 0, -5]
        result = selection_sort(arr)
        self.assertListEqual(result, [-5, -3, -2, -1, 0])


class MergeSortTest(unittest.TestCase):

    def test_merge_five(self):
        arr = [2, 3, 1, 0, 5]
        merge_sort(arr)
        self.assertListEqual(arr, [0, 1, 2, 3, 5])

    def test_merge_empty(self):
        arr = []
        merge_sort(arr)
        self.assertListEqual(arr, [])

    def test_merge_sorted(self):
        arr = [1, 2, 3, 4, 5]
        merge_sort(arr)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])

    def test_merge_negative(self):
        arr = [-2, -3, -1, 0, -5]
        merge_sort(arr)
        self.assertListEqual(arr, [-5, -3, -2, -1, 0])


def run_lab1_tests():
    unittest.main()


if __name__ == "__main__":
    run_lab1_tests()
