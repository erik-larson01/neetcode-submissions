class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)

        # DP[i][a] = # ways to form amount a with coins from index i onward
        # Result is at DP[0][amount]

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # For amount 0, there is 1 way
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for amnt in range(amount + 1):
                if amnt >= coins[i]:
                    # Coin can be taken, take and skip
                    dp[i][amnt] = dp[i + 1][amnt] # skip
                    dp[i][amnt] += dp[i][amnt - coins[i]]


        return dp[0][amount]