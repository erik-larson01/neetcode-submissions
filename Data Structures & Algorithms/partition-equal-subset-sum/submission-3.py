class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        # DP[i]j] = whether we can/can't parition the first i numbers
        # to form sum j
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True # We can always take nothing for sum 0
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # Either take or do not take (only take if possible)
                if nums[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - nums[i - 1]])
                else:
                    # Do not take
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]

    