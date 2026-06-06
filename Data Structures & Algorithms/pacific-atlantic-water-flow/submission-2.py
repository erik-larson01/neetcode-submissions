class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            # Check bounds to ensure the cell is not in the ocean
            # Also reverse the condition, check if the current cell > prev cell
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or heights[r][c] < prevHeight:
                return
            
            # Current cell is taller than prev cell, current cell can reach ocean

            # Mark cell as visited, where visited is the ocean it can reach
            visited.add((r, c))

            # Traverse in all directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Run DFS from every cell that borders the atlantic and the pacific
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0]) # Left pacific boundary
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) # Right atlantic boundary

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c]) # Top pacific boundary
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) # Bottom atlantic boundary

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    # Cell [r, c] can reach both oceans
                    res.append([r, c])
        return res
        