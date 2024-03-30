class Solution:
    def solveNQueens(self, n):
        def Queens(row, board):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if (
                    col not in vertical
                    and (row - col) not in diagonalleft
                    and (row + col) not in diagonalright
                ):
                    board[row][col] = "Q"
                    vertical.add(col)
                    diagonalleft.add(row - col)
                    diagonalright.add(row + col)
                    Queens(row + 1, board)
                    board[row][col] = "."
                    vertical.remove(col)
                    diagonalleft.remove(row - col)
                    diagonalright.remove(row + col)

        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        vertical, diagonalleft, diagonalright = set(), set(), set()
        Queens(0, board)
        return res