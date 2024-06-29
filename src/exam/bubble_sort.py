import unittest

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


class BubbleSortTest(unittest.TestCase):

    def test_bubble_3(self):
        arr = [2,1,3,5,4,7]
        sorted_arr = [1,2,3,4,5,7]
        self.assertListEqual(bubble_sort(arr), sorted_arr)

    def test_bubble_sorted(self):
        arr = [1,2,3,4,5,6,7]
        sorted_arr = [1,2,3,4,5,6,7]
        self.assertListEqual(bubble_sort(arr), sorted_arr)
    
    def test_bubble_empty(self):
        arr = []
        sorted_arr = []
        self.assertListEqual(bubble_sort(arr), sorted_arr)


if __name__=="__main__":
    unittest.main()