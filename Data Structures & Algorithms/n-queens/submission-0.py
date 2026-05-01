class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            # If all n rows are filled with valid queens
            if row == n:
                # Append board as list of strings
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                if self.isSafePosition(row, col, board):
                    # Place the queen, recurse to the next row, then backtrack
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
        backtrack(0)
        return res

    # Checks if the current position at (row, col) is safe for a queen placed in previous rows
    # As we place queens top down every row, there cannot be queens below or left of (row, col)
    def isSafePosition(self, row, col, board):
        # Check if there is a queen above
        rowToCheck = row - 1
        while rowToCheck >= 0:
            if board[rowToCheck][col] == "Q":
                return False
            rowToCheck -= 1
        
        # Check if there is a queen on the top left diagonal
        rowToCheck, colToCheck = row - 1, col - 1
        while rowToCheck >= 0 and colToCheck >= 0:
            if board[rowToCheck][colToCheck] == "Q":
                return False
            rowToCheck -= 1
            colToCheck -= 1

        # Check if there is a queen on the top right diagonal
        rowToCheck, colToCheck = row - 1, col + 1
        while rowToCheck >= 0 and colToCheck < len(board):
            if board[rowToCheck][colToCheck] == "Q":
                return False
            rowToCheck -= 1
            colToCheck += 1
        return True