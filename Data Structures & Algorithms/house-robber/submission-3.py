class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # For each house, either take or do not take
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]
