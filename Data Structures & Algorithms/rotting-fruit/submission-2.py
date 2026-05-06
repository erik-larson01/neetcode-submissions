class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Store all rotten fruit in the queue and set fresh count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                # For every direction, check neighbors and make them rotten
                for dirRow, dirCol in directions:
                    row, col = r + dirRow, c + dirCol
                    # Checl bounds and freshness per neighbor
                    if (row >= 0 and col >= 0 and row < ROWS and 
                        col < COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1