import unittest

def partition(arr, p, r):
    # let the pivot be the last element
    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = x, arr[i+1]

    return i+1
    
    
def quick_sort(arr, p: int = 0, r: int | None = None):
    if r is None:
        r = len(arr) - 1

    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)
    return arr



class QuickSortTest(unittest.TestCase):

    def test_quick_3(self):
        arr = [2,1,3,5,4,7]
        sorted_arr = [1,2,3,4,5,7]
        self.assertListEqual(quick_sort(arr), sorted_arr)

    def test_quick_sorted(self):
        arr = [1,2,3,4,5,6,7]
        sorted_arr = [1,2,3,4,5,6,7]
        self.assertListEqual(quick_sort(arr), sorted_arr)
    
    def test_quick_empty(self):
        arr = []
        sorted_arr = []
        self.assertListEqual(quick_sort(arr), sorted_arr)


if __name__=="__main__":
    unittest.main()