class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or 
                c == COLS or board[r][c] != "O"):
                return
            
            # Cell is "O", mark cell as temp "T"
            board[r][c] = "T"

            # Traverse
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Run DFS on all edge "O"s
        for r in range(ROWS):
            if board[r][0] == "O": # Left boundary
                dfs(r, 0)
            if board[r][COLS - 1] == "O": # Right boundary
                dfs(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O": # Top boundary
                dfs(0, c)
            if board[ROWS - 1][c] == "O": # Bottom boundary
                dfs(ROWS - 1, c)
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    # Any "O" is safe, turn to "X"
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    # Any "T" is safe, turn to "O"
                    board[r][c] = "O"


