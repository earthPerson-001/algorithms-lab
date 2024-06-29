import unittest

from setup_test import setup_paths  # to setup the paths and other related things

setup_paths()

from src.lab3.knapsack_0_1_bruteforce import knapsack_0_1_bruteforce
from src.lab3.knapsack_fractional_bruteforce import knapsack_fractional_bruteforce
from src.lab3.knapsack_fractional_greedy import knapsack_fractional_greedy
from src.lab3.knapsack_0_1_dynamic import knapsack_0_1_dynamic


class Knapsack_0_1_Bruteforce(unittest.TestCase):

    def test_all_full(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 50
        result = knapsack_0_1_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 1])

    def test_empty(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 0
        result = knapsack_0_1_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [0, 0, 0])

    def test_two_full(self):
        profits = [100, 200, 300]
        weights = [10, 20, 60]
        max_capacity = 50
        result = knapsack_0_1_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 0])


class Knapsack_Fractional_Bruteforce(unittest.TestCase):

    def test_all_full(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 50
        result = knapsack_fractional_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 1])

    def test_empty(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 0
        result = knapsack_fractional_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [0, 0, 0])

    def test_two_full_and_a_fraction(self):
        profits = [100, 200, 300]
        weights = [10, 20, 60]
        max_capacity = 50
        result = knapsack_fractional_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 1 / 3])

    def test_three_and_a_fraction(self):
        profits = [100, 200, 300, 400]
        weights = [10, 20, 60, 101]
        max_capacity = 100
        result = knapsack_fractional_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 1, 10 / 101])

    def test_a_fraction(self):
        profits = [10, 15, 500]
        weights = [3, 4, 9]
        max_capacity = 8
        result = knapsack_fractional_bruteforce(profits, weights, max_capacity)
        self.assertListEqual(result, [0, 0, 8 / 9])

    def test_(self):
        weights = [1, 3, 4, 5]
        profits = [1, 4, 5, 7]
        capacity = 7
        result = knapsack_fractional_bruteforce(profits, weights, capacity)
        self.assertEqual(result, [0, 2 / 3, 0, 1])


class Knapsack_Fractional_Greedy(unittest.TestCase):

    def test_all_full(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 50
        result = knapsack_fractional_greedy(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 1])

    def test_empty(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 0
        result = knapsack_fractional_greedy(profits, weights, max_capacity)
        self.assertListEqual(result, [0, 0, 0])

    def test_two_full_and_a_fraction(self):
        profits = [100, 200, 300]
        weights = [10, 20, 60]
        max_capacity = 50
        result = knapsack_fractional_greedy(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 1 / 3])

    def test_three_and_a_fraction(self):
        profits = [100, 200, 300, 400]
        weights = [10, 20, 60, 101]
        max_capacity = 100
        result = knapsack_fractional_greedy(profits, weights, max_capacity)
        self.assertListEqual(result, [1, 1, 1, 10 / 101])


class Knapsack_0_1_Dynamic(unittest.TestCase):

    def test_all_full(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 50
        result = knapsack_0_1_dynamic(profits, weights, max_capacity)
        self.assertEqual(result, 600)

    def test_empty(self):
        profits = [100, 200, 300]
        weights = [10, 20, 20]
        max_capacity = 0
        result = knapsack_0_1_dynamic(profits, weights, max_capacity)
        self.assertEqual(result, 0)

    def test_two_full(self):
        profits = [100, 200, 300]
        weights = [10, 20, 60]
        max_capacity = 50
        result = knapsack_0_1_dynamic(profits, weights, max_capacity)
        self.assertEqual(result, 300)

    def test_knapsack_non_fractional(self):
        weights = [2, 1, 1, 1]
        profits = [3, 4, 5, 6]
        capacity = 5
        result = knapsack_0_1_dynamic(profits, weights, capacity)
        self.assertEqual(result, 18)

        weights = [3]
        profits = [10]
        capacity = 5
        result = knapsack_0_1_dynamic(profits, weights, capacity)
        self.assertEqual(result, 10)

        weights = [1, 2, 3]
        profits = [6, 10, 12]
        capacity = 6
        result = knapsack_0_1_dynamic(profits, weights, capacity)
        self.assertEqual(result, 28)

        weights = [1, 3, 4, 5]
        profits = [1, 4, 5, 7]
        capacity = 7
        result = knapsack_0_1_dynamic(profits, weights, capacity)
        self.assertEqual(result, 9)

        weights = [2, 2, 2]
        profits = [10, 20, 30]
        capacity = 4
        result = knapsack_0_1_dynamic(profits, weights, capacity)
        self.assertEqual(result, 50)

        weights = [1, 2, 3]
        profits = [10, 20, 30]
        capacity = 6
        result = knapsack_0_1_dynamic(profits, weights, capacity)
        self.assertEqual(result, 60)


if __name__ == "__main__":
    unittest.main()
