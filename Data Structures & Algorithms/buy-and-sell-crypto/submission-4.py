class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0,1 # L is sell, R is buy
        while r < len(prices):
            # Check if profit exists
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else: 
                # Update buy day to the previous sell day as l < r.
                l = r
            # Try next value
            r += 1
        return profit