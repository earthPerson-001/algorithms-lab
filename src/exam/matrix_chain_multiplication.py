import sys
import unittest


def bruteforce_matrix_chain_multiplication(
    dimensions: list[int], i: int | None = None, j: int | None = None
):
    if i == None:
        i = 0

    if j == None:
        j = len(dimensions) - 2

    if i == j:
        return 0

    min_multiplications = sys.maxsize
    for k in range(i + 1, j + 1):
        current_multiplications = (
            bruteforce_matrix_chain_multiplication(dimensions, i, k - 1)
            + bruteforce_matrix_chain_multiplication(dimensions, k, j)
            + dimensions[i] * dimensions[k] * dimensions[j + 1]
        )
        if current_multiplications < min_multiplications:
            min_multiplications = current_multiplications

    return min_multiplications


def dynamic_memo_matrix_chain_multiplication(
    dimensions: list[int], i: int | None = None, j: int | None = None, memo=None
):
    if memo is None:
        i = 0
        n = len(dimensions) - 1
        j = n - 1
        memo = [[None for _ in range(n)] for _ in range(n)]

    if i == j:
        return 0

    if memo[i][j] is not None:
        return memo[i][j]

    min_multiplications = sys.maxsize
    for k in range(i + 1, j + 1):
        current_multiplications = (
            dynamic_memo_matrix_chain_multiplication(dimensions, i, k - 1, memo)
            + dynamic_memo_matrix_chain_multiplication(dimensions, k, j, memo)
            + dimensions[i] * dimensions[k] * dimensions[j + 1]
        )
        if current_multiplications < min_multiplications:
            min_multiplications = current_multiplications
            memo[i][j] = min_multiplications

    return min_multiplications


def dynamic_matrix_chain_multiplication(dimensions: list[int]):
    """
    Dimension is of length n+1 for n matrixes

    Eg: first matrix if of dimension dimensions[0] * dimensions[1]
    """
    n = len(dimensions) - 1
    # creating a table of length n*n to store the results
    tab = [[None for _ in range(n)] for _ in range(n)]

    # There is no multiplication required for single matrix
    for i in range(n):
        tab[i][i] = 0

    # for storing the sequence which produced minimum multiplications
    s = [[None for _ in range(n - 1)] for _ in range(n - 1)]

    for chain_length in range(1, n):
        for i in range(n - chain_length):
            j = i + chain_length
            min_multiplications = sys.maxsize
            for k in range(i + 1, j + 1):
                current_multiplications = (
                    tab[i][k - 1]
                    + tab[k][j]
                    + dimensions[i] * dimensions[k] * dimensions[j + 1]
                )
                if current_multiplications < min_multiplications:
                    min_multiplications = current_multiplications
                    tab[i][j] = min_multiplications
                    s[i][j - 1] = k
    return tab[0][n - 1]


class TestDynamicTabulationMatrixChainMultiplication(unittest.TestCase):

    def test_dynamic_tabulation_matrix_chain_multiplication(self):
        dimensions = [5, 4, 6, 2, 7]
        expected = 158

        self.assertEqual(dynamic_matrix_chain_multiplication(dimensions), expected)


class TestBruteforceRecursiveMatrixChainMultiplication(unittest.TestCase):

    def test_bruteforce_recursive_matrix_chain_multiplication(self):
        dimensions = [5, 4, 6, 2, 7]
        expected = 158

        self.assertEqual(bruteforce_matrix_chain_multiplication(dimensions), expected)


class TestDynamicRecursiveMatrixChainMultiplication(unittest.TestCase):

    def test_dynamic_recursive_matrix_chain_multiplication(self):
        dimensions = [5, 4, 6, 2, 7]
        expected = 158

        self.assertEqual(dynamic_memo_matrix_chain_multiplication(dimensions), expected)


if __name__ == "__main__":
    unittest.main()
