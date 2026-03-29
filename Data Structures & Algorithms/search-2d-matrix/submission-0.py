class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])

        # Define pointers to search over rows first
        top, bottom = 0, numRows - 1
        while top <= bottom:
            midRow = (top + bottom) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bottom = midRow - 1
            else:
                # Target in row
                break

        # Check if valid row found
        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        # Row identified, search inside that row
        l,r = 0, numCols - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False