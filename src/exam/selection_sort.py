import unittest

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        if smallest != i:
            arr[smallest],arr[i] = arr[i],arr[smallest]
    return arr

class SelectionSortTest(unittest.TestCase):

    def test_selection_3(self):
        arr = [2,1,3,5,4,7]
        sorted_arr = [1,2,3,4,5,7]
        self.assertListEqual(selection_sort(arr), sorted_arr)

    def test_selection_sorted(self):
        arr = [1,2,3,4,5,6,7]
        sorted_arr = [1,2,3,4,5,6,7]
        self.assertListEqual(selection_sort(arr), sorted_arr)
    
    def test_selection_empty(self):
        arr = []
        sorted_arr = []
        self.assertListEqual(selection_sort(arr), sorted_arr)


if __name__=="__main__":
    unittest.main()
