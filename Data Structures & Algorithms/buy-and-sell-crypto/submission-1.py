class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            buy_start = prices[i]
            for j in range(i + 1, len(prices)):
                potential_sell = prices[j]
                profit = max(profit, potential_sell - buy_start)            
        return profit