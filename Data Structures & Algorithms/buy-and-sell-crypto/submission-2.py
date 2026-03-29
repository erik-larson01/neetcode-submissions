class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = 0
        profit = 0
        for i in range(1, len(prices)):
            min_buy = math.inf
            sell = prices[i]
            for j in range(i):
                min_buy = min(min_buy, prices[j])
            profit = max(profit, sell - min_buy)
            
        return profit