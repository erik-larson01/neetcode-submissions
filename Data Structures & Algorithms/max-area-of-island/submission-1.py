class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        def dfs(r, c, area):
            # If 0 or row, col out of bounds - do not increment area
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return area
            
            # Sink the tile
            grid[r][c] = 0
            
            islandArea = area + 1

            # Traverse to sink the entire island
            islandArea = dfs(r - 1, c, islandArea) # Up
            islandArea = dfs(r + 1, c, islandArea) # Down
            islandArea = dfs(r, c - 1, islandArea) # Left
            islandArea = dfs(r, c + 1, islandArea) # Right
            
            return islandArea
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col, 0))

        return area