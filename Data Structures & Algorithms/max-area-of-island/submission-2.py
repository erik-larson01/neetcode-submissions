class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        def dfs(r, c):
            # If 0 or row, col out of bounds - do not increment area
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            # Sink the tile
            grid[r][c] = 0

            # Traverse to sink the entire island
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col))

        return area