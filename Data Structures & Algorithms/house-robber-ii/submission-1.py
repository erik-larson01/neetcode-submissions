class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        # Rob houses from 1 to n - 1 (exclude first)
        dp1 = [0] * n
        dp1[1] = nums[1]
        if n > 2:
            dp1[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        # Rob houses from 0 to n - 2 (exclude last)
        dp2 = [0] * n
        dp2[0] = nums[0]
        dp2[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        return max(dp1[n - 1], dp2[n - 2])