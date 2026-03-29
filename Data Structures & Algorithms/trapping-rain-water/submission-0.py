class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i, len(height)):
                rightMax = max(rightMax, height[j])

            res += min(leftMax, rightMax) - height[i]
        return res