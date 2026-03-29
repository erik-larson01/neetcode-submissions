class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])
        topRow = 0
        bottomRow = numRows - 1

        while topRow <= bottomRow:
            midRow = (topRow + bottomRow) // 2
            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            elif target < matrix[midRow][0]:
                bottomRow = midRow - 1
            else: 
                # Row found
                break
        
        if not (topRow <= bottomRow):
            # Value not found
            return False
        
        rowNum = (topRow + bottomRow) // 2
        l,r = 0, numCols - 1
        
        while l <= r:
            m = (l + r) // 2
            if target > matrix[rowNum][m]:
                l = m + 1
            elif target < matrix[rowNum][m]:
                r = m - 1
            else:
                return True
        return False