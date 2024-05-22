import unittest

from setup_test import setup_paths  # to setup the paths and other related things

setup_paths()

from src.lab2.merge_sort import merge_sort, merge
from src.lab2.quick_sort import quick_sort, partition


class MergeSortTest(unittest.TestCase):

    def test_merge_sort_five(self):
        arr = [2, 3, 1, 0, 5]
        result = merge_sort(arr)
        self.assertListEqual(result, [0, 1, 2, 3, 5])

    def test_merge_sort_empty(self):
        arr = []
        result = merge_sort(arr)
        self.assertListEqual(result, [])

    def test_merge_sort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = merge_sort(arr)
        self.assertListEqual(result, [1, 2, 3, 4, 5])
    
    def test_merge_five(self):
        arr1 = [1,2,3,5]
        arr2 = [3,5,7,9]
        result = merge(arr1 + arr2, 0, 3, 7)
        self.assertListEqual(result,[1,2,3,3,5,5,7,9])

    def test_merge_empty(self):
        arr = []
        result = merge(arr, 0, 0, 0)
        self.assertListEqual(result, [])

    def test_merge_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = merge(arr, 0, 2, 4)
        self.assertListEqual(result, [1, 2, 3, 4, 5])


class QuickSortTest(unittest.TestCase):

    def test_quick_five(self):
        arr = [2, 3, 1, 0, 5]
        result = quick_sort(arr)
        self.assertListEqual(result, [0, 1, 2, 3, 5])

    def test_quick_empty(self):
        arr = []
        result = quick_sort(arr)
        self.assertListEqual(result, [])

    def test_quick_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = quick_sort(arr)
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    def test_partition_three(self):
        arr = [1, 3, 2]
        q = partition(arr, 0, 2)
        self.assertEqual(q, 1)
        self.assertListEqual(arr, [1, 2, 3])

    def test_partition_three_not_all_indices(self):
        arr = [1, 3, 2]
        q = partition(arr, 0, 1)
        self.assertEqual(q, 1)
        self.assertListEqual(arr, [1, 3, 2])

    def test_partition_five(self):
        arr = [1, 5, 3, 4, 2]
        q = partition(arr, 0, 4)
        self.assertEqual(q, 1)
        self.assertListEqual(arr, [1, 2, 3, 4, 5])

    def test_partition_five_not_all_indices(self):
        arr = [1, 5, 3, 4, 2]
        q = partition(arr, 0, 3)
        self.assertEqual(q, 2)
        self.assertListEqual(arr, [1, 3, 4, 5, 2])


if __name__ == "__main__":
    unittest.main()
