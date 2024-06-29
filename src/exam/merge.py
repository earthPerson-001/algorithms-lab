import unittest


def merge(left, right):
    merged = [None for _ in range(len(left) + len(right))]
    j, k = 0, 0

    for i in range(len(merged)):

        if j >= len(left):
            merged[i:] = right[k:]
            break
        elif k >= len(right):
            merged[i:] = left[j:]
            break

        if left[j] <= right[k]:
            merged[i] = left[j]
            j += 1
        else:
            merged[i] = right[k]
            k += 1
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


class SelectionSortTest(unittest.TestCase):

    def test_merge_3(self):
        arr = [2, 1, 3, 5, 4, 7]
        sorted_arr = [1, 2, 3, 4, 5, 7]
        self.assertListEqual(merge_sort(arr), sorted_arr)

    def test_merge_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        sorted_arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertListEqual(merge_sort(arr), sorted_arr)

    def test_merge_empty(self):
        arr = []
        sorted_arr = []
        self.assertListEqual(merge_sort(arr), sorted_arr)


if __name__ == "__main__":
    unittest.main()
