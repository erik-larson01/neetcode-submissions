class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Add all rotten fruit to the queue for multisource bfs
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            # Multi source bfs, start all at once
            for i in range(len(q)):
                r, c = q.popleft()
                # Check neighbors for freshness
                for dx, dy in directions:
                    row, col = r + dx, c + dy
                    if (row >= 0 and col >= 0 and row < ROWS and col < COLS
                        and grid[row][col] == 1):
                        # Fresh found, make it rotten and add it
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            minutes += 1
        
        return minutes if fresh == 0 else -1
        
