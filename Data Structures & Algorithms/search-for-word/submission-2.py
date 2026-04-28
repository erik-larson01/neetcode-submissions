class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        # Current row of board, col of board, and index within word
        def dfs(row, col, i):
            # Check if all chars match the word
            if i == len(word):
                return True 

            # Check row, col out of bounds
            if min(row, col) < 0 or row >= ROWS or col >= COLS:
                return False
            
            # Check if we have visited this cell before
            if (row, col) in path:
                return False

            # Check if tile matches
            if board[row][col] != word[i]:
                return False
            
            # Tile matches, check neighbors then backtrack
            path.add((row, col))
            res = (dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1))
            path.remove((row, col))

            return res
        
        # For every tile, attempt to start the word there
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    # Word found
                    return True
        return False