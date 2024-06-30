import unittest
from typing import Callable
from typing import Any


def counting_sort(array, k: int | None = None, start: int = 0, key : None | Callable[..., int] = None):

    n = len(array)  # total number of elements

    if k is None:
        if key is None:
            k = max(array)
        else:
            k = max(map(key, array))

    # creating an array of width (end - start + 1) to store the occurances of the numbers
    c = [0] * (k - start + 1)

    # storing the occurance of the numbers
    if key is not None:
        array_digits = list(map(key, array))
    else:
        array_digits = array
    for num in array_digits:
        c[num - start] += 1

    # calculating the cumulative sum
    for i in range(1, k - start + 1):
        c[i] = c[i - 1] + c[i]

    # sorting from end
    output_array = array[:]
    for num in range(n - 1, -1, -1):
        output_array[c[array_digits[num] - start] - 1] = array[num]
        c[array_digits[num] - start] -= 1

    return output_array

def digit_extractor(number, to_extract):
    "extracts the nth digit from right"
    digit = number
    remainder = 0
    for i in range(0, to_extract):
        remainder = digit % 10
        if i < to_extract - 1:
            digit = digit // 10

    return remainder

def radix_sort(array: list[int]):
    maximum_element = max(array)
    n_digits = 0
    while(maximum_element > 0):
        maximum_element = maximum_element // 10
        n_digits+=1


    for i in range(1, n_digits + 1):
        array = counting_sort(array, key = lambda x: digit_extractor(x, i))

    return array


class CountingSortTest(unittest.TestCase):

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



class RadixSortTest(unittest.TestCase):

    def test_radix_6(self):
        arr = [2, 1, 3, 5, 6, 4, 7]
        sorted_arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertListEqual(radix_sort(arr), sorted_arr)

    def test_radix_sorted(self):
        arr = [2, 3, 4, 5, 6, 7]
        sorted_arr = [2, 3, 4, 5, 6, 7]
        self.assertListEqual(radix_sort(arr), sorted_arr)

    def test_radix_from_ten(self):
        arr = [10, 15, 14, 13, 11, 20, 19]
        sorted_arr = [10, 11, 13, 14, 15, 19, 20]
        self.assertListEqual(radix_sort(arr), sorted_arr)
    
    def test_radix_from_hundred(self):
        arr = [100, 105, 104, 133, 121, 210, 159]
        sorted_arr = [100, 104, 105, 121, 133, 159, 210]
        self.assertListEqual(radix_sort(arr), sorted_arr)


if __name__ == "__main__":
    unittest.main()
