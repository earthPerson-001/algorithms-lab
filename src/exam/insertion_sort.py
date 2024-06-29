import unittest

def insertion_sort(arr):
    for i in range(1, len(arr)):
        swap_with = arr[i]
        j = i - 1

        while (j >= 0 and swap_with < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = swap_with

    return arr


class InsertionSortTest(unittest.TestCase):

    def test_insertion_3(self):
        arr = [2,1,3,5,4,7]
        sorted_arr = [1,2,3,4,5,7]
        self.assertListEqual(insertion_sort(arr), sorted_arr)

    def test_insertion_sorted(self):
        arr = [1,2,3,4,5,6,7]
        sorted_arr = [1,2,3,4,5,6,7]
        self.assertListEqual(insertion_sort(arr), sorted_arr)
    
    def test_insertion_empty(self):
        arr = []
        sorted_arr = []
        self.assertListEqual(insertion_sort(arr), sorted_arr)


if __name__=="__main__":
    unittest.main()