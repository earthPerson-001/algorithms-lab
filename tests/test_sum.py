import unittest

from setup_test import setup_paths # to setup the paths and other related things
setup_paths()

from src.lab1.sum import sum


class SumTest(unittest.TestCase):
    
    def test_sum_three(self):
        arr = [2,3,4]
        result = sum(arr)
        self.assertEqual(result, 9)
        
    def test_sum_invalid(self):
        arr = [1,2,3]
        result = sum(arr)
        self.assertNotEqual(result, 7)
        
    def test_sum_four(self):
        arr = [1,2,3,4]
        result = sum(arr)
        self.assertEqual(result, 10)
        
    def test_sum_empty(self):
        arr = []
        result = sum(arr)
        self.assertEqual(result, 0)
    
if __name__=='__main__':
    unittest.main()
