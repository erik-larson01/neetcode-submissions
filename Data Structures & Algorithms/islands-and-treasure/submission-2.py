class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        # Adds a valid tile of the grid to the queue
        def addValidCell(r, c):
            if (r >= 0 and c >= 0 and r < ROWS and c < COLS 
                and (r, c) not in visited and grid[r][c] != -1):
                visited.add((r, c))
                q.append([r, c])
        
        # Find all treasures and add to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        # BFS
        dist = 0
        while q:
            # Try all neighbors/directions
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addValidCell(r + 1, c)
                addValidCell(r - 1, c)
                addValidCell(r, c + 1)
                addValidCell(r, c - 1)
            dist += 1
        
