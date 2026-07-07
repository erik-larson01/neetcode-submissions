class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        # DP[i] is the minumum # of coins to make amount i
        # Result at DP[amount]

        dp[0] = 0

        for amnt in range(1, amount + 1):
            for c in coins:
                if amnt - c >= 0:
                    dp[amnt] = min(dp[amnt], 1 + dp[amnt - c])
        return dp[amount] if dp[amount] != amount + 1 else -1