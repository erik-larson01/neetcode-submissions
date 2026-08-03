class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (i, holding) -> profit from day i

        # If we are holding, we cannot buy and can only sell
        # If we are not holding, we can buy
        def dfs(i, holding):
            if i >= len(prices):
                return 0
            
            if (i, holding) in dp:
                return dp[(i, holding)]

            # Calculate option to skip
            skip = dfs(i + 1, holding)

            if holding:
                # Either sell or skip
                sell = dfs(i + 2, not holding) + prices[i]
                dp[(i,holding)] = max(sell, skip)
            else:
                # Either buy or skip
                buy = dfs(i + 1, not holding) - prices[i]
                dp[(i, holding)] = max(buy, skip)
            return dp[(i, holding)]
        return dfs(0, False)