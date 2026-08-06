class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][holding] = max profit at day i
        # holding == 1 if we are holding, else 0
        dp = [[0] * 2 for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for holding in [True, False]:
                if holding:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else - prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)
        return dp[0][True]