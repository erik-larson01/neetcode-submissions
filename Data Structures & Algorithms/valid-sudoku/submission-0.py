class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Row -> Nums in Row 
        cols = defaultdict(set) # Col -> Nums in Col 
        squares = defaultdict(set) # Square (0,0 to 2,2) -> Nums in Square

        # 9x9 Grid
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                if n in rows[r] or n in cols[c] or n in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(n)
                cols[c].add(n)
                squares[(r // 3, c // 3)].add(n)
        return True
                