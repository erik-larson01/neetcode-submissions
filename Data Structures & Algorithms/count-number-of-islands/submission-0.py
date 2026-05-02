class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 # Num islands

        # When a 1 is encountered, "sink" entire island
        def dfs(row, col):
            # Check bounds and if tile is a "0"
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0"):
                return
            
            # "Sink" tile by setting it to "0"
            grid[row][col] = "0"
            
            # Continue recursion by traveling all four directions
            dfs(row + 1, col) # Down
            dfs(row - 1, col) # Up
            dfs(row, col + 1) # Right 
            dfs(row, col - 1) # Left
        
        # Go tile by tile
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res