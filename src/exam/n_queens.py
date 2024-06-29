def check_safe(board, x, y, n):
    # checking if there are other queens in the same column
    for i in range(x):
        if board[i][y] == 1:
            return False

    # checking if there are other queens in the left diagonal
    row = x - 1
    col = y - 1
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # checking if there are other queens in the right diagonal
    row = x - 1
    col = y + 1
    while row >= 0 and col < n:
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def n_queens(n: int):
    board = [[0 for _ in range(n)] for _ in range(n)]

    def n_queens_helper(x, n):
        if x >= n:
            return True

        for col in range(n):
            if check_safe(board, x, col, n):
                board[x][col] = 1
                if n_queens_helper(x + 1, n):
                    return True
                else:
                    board[x][col] = 0
        return False

    out = n_queens_helper(0, n)
    return out, board


if __name__ == "__main__":
    print(n_queens(4))
