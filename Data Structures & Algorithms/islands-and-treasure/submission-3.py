class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        def addValidTile(r, c):
            if (r >= 0 and c >= 0 and r < ROWS and c < COLS and 
                grid[r][c] != -1 and (r, c) not in visited):
                visited.add((r,c))
                q.append((r, c))
        
        # Add all treasures to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # BFS
        distance = 0
        while q:
            for i in range(len(q)): 
                r, c = q.popleft()
                grid[r][c] = distance

                # Try neighbors
                addValidTile(r + 1, c)
                addValidTile(r - 1, c)
                addValidTile(r, c + 1)
                addValidTile(r, c - 1)
            distance += 1
        