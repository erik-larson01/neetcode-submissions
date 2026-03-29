class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0,1 # L is sell, R is buy
        while r < len(prices):
            # Check if profit
            if prices[r] - prices[l] > 0:
                profit = max(profit, prices[r] - prices[l])
            else: 
                # No profit, update both pointers
                l = r
            # Try next value
            r += 1
        return profit