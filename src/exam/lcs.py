import unittest


def recursive_lcs(seq1, seq2, m: int | None = None, n: int | None = None):
    if m is None:
        m = len(seq1) - 1

    if n is None:
        n = len(seq2) - 1

    if m < 0 or n < 0:
        return 0

    if seq1[m] == seq2[n]:
        return 1 + recursive_lcs(seq1, seq2, m - 1, n - 1)
    else:
        return max(
            recursive_lcs(seq1, seq2, m - 1, n), recursive_lcs(seq1, seq2, m, n - 1)
        )


def memo_recursive_lcs(
    seq1,
    seq2,
    m: int | None = None,
    n: int | None = None,
    memo: list[int] | None = None,
):

    if memo is None:
        m = len(seq1) - 1
        n = len(seq2) - 1
        memo = [[None for _ in range(n + 1)] for _ in range(m + 1)]
    else:
        if memo[m][n] is not None:
            return memo[m][n]

    if m < 0 or n < 0:
        return 0

    if seq1[m] == seq2[n]:
        ret_val = 1 + memo_recursive_lcs(seq1, seq2, m - 1, n - 1, memo)
    else:
        ret_val = max(
            memo_recursive_lcs(seq1, seq2, m - 1, n, memo),
            memo_recursive_lcs(seq1, seq2, m, n - 1, memo),
        )

    memo[m][n] = ret_val
    return ret_val


def tabulation_lcs(seq1, seq2):
    n = len(seq1)
    m = len(seq2)

    # construct a table of size (n + 1) by (m + 1)
    table = [[None for _ in range(m + 1)] for _ in range(n + 1)]

    # filling the very first row and column with zeroes
    table[0] = [0] * (m + 1)
    for i in range(1, n + 1):
        table[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j -1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    sequence=""
    i = n
    j = m
    while(i >= 0 and j >= 0):
        if table[i][j] != max(table[i-1][j], table[i][j-1]):
            i-=1
            j-=1
            sequence += seq1[i]
        elif table[i-1][j] > table[i][j-1] :
            i-=1
        else:
            j-=1


    return table[n][m], sequence[::-1]
    

class TestRecursiveLcs(unittest.TestCase):

    def test_recursive_lcs_three(self):
        seq1 = "abcd"
        seq2 = "acd"
        expected = len("acd")

        self.assertEqual(recursive_lcs(seq1, seq2), expected)


class TestDynamicRecursiveLcs(unittest.TestCase):

    def test_memo_recursive_lcs_three(self):
        seq1 = "abcd"
        seq2 = "acd"
        expected = len("acd")

        self.assertEqual(memo_recursive_lcs(seq1, seq2), expected)


class TestDynamicIterativeLcs(unittest.TestCase):

    def test_tabular_iterative_lcs_three(self):
        seq1 = "abcd"
        seq2 = "acd"
        expected_seq = "acd"
        expected_len = len(expected_seq)

        seq_len, seq = tabulation_lcs(seq1, seq2)

        self.assertEqual(seq_len, expected_len)
        self.assertEqual(seq, expected_seq)


if __name__ == "__main__":
    unittest.main()
