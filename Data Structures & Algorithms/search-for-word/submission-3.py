class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                # Word found
                return True
            
            # Check if index is out of board bounds
            if min(row, col) < 0 or row >= ROWS or col >= COLS:
                return False

            # Check if tile already found or does not match
            if (row, col) in path or board[row][col] != word[i]:
                return False
            
            path.add((row, col))
            res = (dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1))
            path.remove((row, col))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False