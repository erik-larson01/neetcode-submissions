class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1 # L is buy day, R is sell day
        profit = 0

        while r < len(prices):
            # Check if profit exists
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                # No profit exists, we found a cheaper buy price so move L
                l = r
            r += 1

        return profit