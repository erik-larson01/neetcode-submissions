class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        res = 0

        # Init leftMax and rightMax to the height of ends of the array
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax: # Equal to min(leftMax, rightMax) = leftMax
                # Water at l is dependent on ONLY leftMax
                # Compute water after moving to avoid negatives
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                # Water at r is dependent on ONLY rightMax
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
