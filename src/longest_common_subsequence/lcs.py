"""
Author: Bishal Neupane

Various implementations for longest common subsequence problem

"""


def lcs_normal(seq1, seq2, m=0, n=0):
    """
    Returns the length of longest common subsequence between seq1 and seq2
    until m index of seq1 and n index of seq2

    """
    if len(seq1) == m or len(seq2) == n:  # terminating condition
        return 0
    elif seq1[m] == seq2[n]:
        return 1 + lcs_normal(seq1, seq2, m + 1, n + 1)
    else:
        return max(lcs_normal(seq1, seq2, m + 1, n), lcs_normal(seq1, seq2, m, n + 1))


def lcs_memoization(seq1, seq2):
    rows = len(seq1)
    columns = len(seq2)

    memo = [[-1 for _ in range(columns + 1)] for _ in range(rows + 1)]

    def lcs_helper(m, n):
        if len(seq1) == m or len(seq2) == n:  # terminating condition
            retval = 0
        elif seq1[m] == seq2[n]:
            if memo[m + 1][n + 1] != -1:
                return 1 + memo[m + 1][n + 1]
            memo[m + 1][n + 1] = 1 + lcs_helper(m + 1, n + 1)
            retval = memo[m + 1][n + 1]
        else:
            if memo[m + 1][n] == -1:
                memo[m + 1][n] = lcs_helper(m + 1, n)
            if memo[m][n + 1] == -1:
                memo[m][n + 1] = lcs_helper(m, n + 1)
            retval = max(memo[m + 1][n], memo[m][n + 1])
        return retval

    return lcs_helper(0, 0)

