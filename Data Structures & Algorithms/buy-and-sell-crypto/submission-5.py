class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1 # L is sell day, R is buy day
        profit = 0

        while r < len(prices):
            # Check if profit exists
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                # Profit does not exist
                l = r
            r += 1

        return profit