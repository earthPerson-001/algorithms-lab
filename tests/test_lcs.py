import unittest

from setup_test import setup_paths  # to setup the paths and other related things

setup_paths()

from src.longest_common_subsequence.lcs import lcs_normal, lcs_memoization


class LCSNormalTest(unittest.TestCase):

    def test_lcs_normal(self):
        seq1 = "abc"
        seq2 = "adec"
        self.assertEqual(lcs_normal(seq1, seq2), 2)

    def test_lcs_normal_no_common(self):
        seq1 = "abc"
        seq2 = "efg"
        self.assertEqual(lcs_normal(seq1, seq2), 0)

    def test_lcs_normal_no_common(self):
        seq1 = "abc"
        seq2 = "efg"
        self.assertEqual(lcs_normal(seq1, seq2), 0)

    def test_lcs_both_empty(self):
        seq1 = ""
        seq2 = ""
        self.assertEqual(lcs_normal(seq1, seq2), 0)

    def test_lcs_one_empty(self):
        seq1 = "abc"
        seq2 = ""
        self.assertEqual(lcs_normal(seq1, seq2), 0)

        seq1 = ""
        seq2 = "def"
        self.assertEqual(lcs_normal(seq1, seq2), 0)

    def test_lcs_identical(self):
        seq1 = "abcdef"
        seq2 = "abcdef"
        self.assertEqual(lcs_normal(seq1, seq2), 6)

    def test_lcs_subsequence_at_beginning(self):
        seq1 = "abcxyz"
        seq2 = "abcuvw"
        self.assertEqual(lcs_normal(seq1, seq2), 3)

    def test_lcs_subsequence_at_end(self):
        seq1 = "xyzabc"
        seq2 = "uvwabc"
        self.assertEqual(lcs_normal(seq1, seq2), 3)

    def test_lcs_interleaved(self):
        seq1 = "a1b2c3"
        seq2 = "xaybzc"
        self.assertEqual(lcs_normal(seq1, seq2), 3)

    def test_lcs_no_common(self):
        seq1 = "abc"
        seq2 = "def"
        self.assertEqual(lcs_normal(seq1, seq2), 0)

    def test_lcs_subsequence_in_middle(self):
        seq1 = "abcde"
        seq2 = "axcye"
        self.assertEqual(lcs_normal(seq1, seq2), 3)  # 'ace' is the common subsequence

    def test_lcs_repeated_characters(self):
        seq1 = "aaaaaa"
        seq2 = "aa"
        self.assertEqual(lcs_normal(seq1, seq2), 2)

    def test_lcs_palindromes(self):
        seq1 = "racecar"
        seq2 = "carrace"
        self.assertEqual(
            lcs_normal(seq1, seq2), 4
        )  # 'race' or 'carr' are common subsequences

class LCSMemoizationTest(unittest.TestCase):

    def test_lcs_memoization(self):
        seq1 = "abc"
        seq2 = "adec"
        self.assertEqual(lcs_memoization(seq1, seq2), 2)

    def test_lcs_memoization_no_common(self):
        seq1 = "abc"
        seq2 = "efg"
        self.assertEqual(lcs_memoization(seq1, seq2), 0)

    def test_lcs_memoization_no_common(self):
        seq1 = "abc"
        seq2 = "efg"
        self.assertEqual(lcs_memoization(seq1, seq2), 0)

    def test_lcs_both_empty(self):
        seq1 = ""
        seq2 = ""
        self.assertEqual(lcs_memoization(seq1, seq2), 0)

    def test_lcs_one_empty(self):
        seq1 = "abc"
        seq2 = ""
        self.assertEqual(lcs_memoization(seq1, seq2), 0)

        seq1 = ""
        seq2 = "def"
        self.assertEqual(lcs_memoization(seq1, seq2), 0)

    def test_lcs_identical(self):
        seq1 = "abcdef"
        seq2 = "abcdef"
        self.assertEqual(lcs_memoization(seq1, seq2), 6)

    def test_lcs_subsequence_at_beginning(self):
        seq1 = "abcxyz"
        seq2 = "abcuvw"
        self.assertEqual(lcs_memoization(seq1, seq2), 3)

    def test_lcs_subsequence_at_end(self):
        seq1 = "xyzabc"
        seq2 = "uvwabc"
        self.assertEqual(lcs_memoization(seq1, seq2), 3)

    def test_lcs_interleaved(self):
        seq1 = "a1b2c3"
        seq2 = "xaybzc"
        self.assertEqual(lcs_memoization(seq1, seq2), 3)

    def test_lcs_no_common(self):
        seq1 = "abc"
        seq2 = "def"
        self.assertEqual(lcs_memoization(seq1, seq2), 0)

    def test_lcs_subsequence_in_middle(self):
        seq1 = "abcde"
        seq2 = "axcye"
        self.assertEqual(lcs_memoization(seq1, seq2), 3)  # 'ace' is the common subsequence

    def test_lcs_repeated_characters(self):
        seq1 = "aaaaaa"
        seq2 = "aa"
        self.assertEqual(lcs_memoization(seq1, seq2), 2)

    def test_lcs_palindromes(self):
        seq1 = "racecar"
        seq2 = "carrace"
        self.assertEqual(
            lcs_memoization(seq1, seq2), 4
        )  # 'race' or 'carr' are common subsequences




def run_lcs_tests():
    unittest.main()


if __name__ == "__main__":
    run_lcs_tests()
