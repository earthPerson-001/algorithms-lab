import unittest

def bruteforce_sequence_search_iterative(string, sequence):
    n = len(string)
    m = len(sequence)
    for i in range(n):
        j = 0
        while(j < m and sequence[j]==string[i+j]):
            j += 1

        if j == m:
            return i

    return -1

class TestBruteforceSequenceSearchIterative(unittest.TestCase):

    def test_bruteforce_sequence_search_iterative(self):
        string = "apple"
        sequence = "pple"
        expected = 1

        self.assertEqual(bruteforce_sequence_search_iterative(string, sequence), expected)
    
    def test_bruteforce_sequence_search_iterative(self):
        string = "aeroplane"
        sequence = "plane"
        expected = 4

        self.assertEqual(bruteforce_sequence_search_iterative(string, sequence), expected)
    
    def test_bruteforce_sequence_search_iterative(self):
        string = "aeroplane"
        sequence = "ball"
        expected = -1

        self.assertEqual(bruteforce_sequence_search_iterative(string, sequence), expected)


if __name__=="__main__":
    unittest.main()
