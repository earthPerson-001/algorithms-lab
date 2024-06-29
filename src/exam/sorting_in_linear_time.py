import unittest


def counting_sort(array, k: int | None = None, start: int = 0):

    n = len(array)  # total number of elements

    if k is None:
        k = max(array)

    # creating an array of width (end - start + 1) to store the occurances of the numbers
    c = [0] * (k - start + 1)

    # storing the occurance of the numbers
    for num in array:
        c[num - start] += 1

    # calculating the cumulative sum
    for i in range(1, k - start + 1):
        c[i] = c[i - 1] + c[i]

    # sorting from end
    output_array = array[:]
    for num in range(n - 1, -1, -1):
        output_array[c[array[num] - start] - 1] = array[num]
        c[array[num] - start] -= 1

    return output_array


class QuickSortTest(unittest.TestCase):

    def test_counting_6(self):
        arr = [2, 1, 3, 5, 6, 4, 7]
        sorted_arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertListEqual(counting_sort(arr, start=1), sorted_arr)

    def test_counting_sorted(self):
        arr = [2, 3, 4, 5, 6, 7]
        sorted_arr = [2, 3, 4, 5, 6, 7]
        self.assertListEqual(counting_sort(arr, start=2), sorted_arr)

    def test_counting_from_ten(self):
        arr = [10, 15, 14, 13, 11, 20, 19]
        sorted_arr = [10, 11, 13, 14, 15, 19, 20]
        self.assertListEqual(counting_sort(arr, start=10), sorted_arr)


if __name__ == "__main__":
    unittest.main()
