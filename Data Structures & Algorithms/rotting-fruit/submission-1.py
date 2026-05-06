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
                    updatedRow, updatedCol = r + dirRow, c + dirCol
                    # Checl bounds and freshness per neighbor
                    if (updatedRow >= 0 and updatedCol >= 0 and updatedRow < ROWS and 
                        updatedCol < COLS and grid[updatedRow][updatedCol] == 1):
                        grid[updatedRow][updatedCol] = 2
                        q.append((updatedRow, updatedCol))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1