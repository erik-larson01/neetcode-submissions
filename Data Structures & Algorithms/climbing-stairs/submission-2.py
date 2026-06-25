class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            # Memoization - either take a 1 step from i - 1 or a 2 step from i - 2
            # DP needs all combinations, so add the two
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]