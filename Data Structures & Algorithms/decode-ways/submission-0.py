class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = # of combinations for s[i:]
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        # Loop backwards
        for i in range(len(s) - 1, -1, -1):
            # Check for invalid zeroes 
            # (a string starting with zero cannot be decoded on its own)
            if s[i] == "0":
                dp[i] = 0
            else:
                # Take one digit
                dp[i] = dp[i + 1]
             
            # Take two digits
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
        
        return dp[0]