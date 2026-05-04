class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        
        # Make an array to track directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            # Use a visited arr to track previously visited tiles
            visited = [[False] * COLS for i in range(ROWS)]
            visited[r][c] = True
            steps = 0 
            
            # BFS
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    # If we are at a treasure, return the steps to get there
                    if grid[row][col] == 0:
                        return steps
                    
                    # Check all valid directions/neighbors
                    for dirRow, dirCol in directions:
                        newRow, newCol = row + dirRow, col + dirCol
                        
                        if (newRow >= 0 and newCol >= 0 and newRow < ROWS and newCol < COLS
                            and not visited[newRow][newCol] and grid[newRow][newCol] != -1):
                            # Checks passed, visit
                            visited[newRow][newCol] = True
                            q.append((newRow, newCol))
                steps += 1
            return INF
        
        # Do BFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        
