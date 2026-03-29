class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force - find min of the max bars on each side for the container
        # Then subtract the current height of the index and do it for all indices
        res = 0
        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i, len(height)):
                rightMax = max(rightMax, height[j])

            # Can never be negative as leftMax/rightMax are init to the height of the bar itself
            res += min(leftMax, rightMax) - height[i]
        return res