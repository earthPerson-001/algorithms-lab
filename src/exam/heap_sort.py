import unittest
import math


def max_heapify(arr, idx, last_index):
    left, right = idx * 2 + 1, idx * 2 + 2

    largest = idx
    if left <= last_index and arr[left] > arr[idx]:
        largest = left
    if right <= last_index and arr[right] > arr[largest]:
        largest = right

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, largest, last_index)


def build_max_heap(arr: list[int]):

    last_index = len(arr) - 1
    for i in range(math.ceil(last_index / 2) - 1, -1, -1):
        max_heapify(arr, i, last_index)


def heap_sort(arr):
    last_index = len(arr) - 1
    build_max_heap(arr)
    for i in range(last_index, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        last_index -= 1
        max_heapify(arr, 0, last_index)
    return arr


class HeapSortTest(unittest.TestCase):

    def test_heap_sort_3(self):
        arr = [2, 1, 3, 5, 4, 7]
        sorted_arr = [1, 2, 3, 4, 5, 7]
        self.assertListEqual(heap_sort(arr), sorted_arr)

    def test_heap_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        sorted_arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertListEqual(heap_sort(arr), sorted_arr)

    def test_insertion_empty(self):
        arr = []
        sorted_arr = []
        self.assertListEqual(heap_sort(arr), sorted_arr)


if __name__ == "__main__":
    unittest.main()
