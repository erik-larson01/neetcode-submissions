class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP[i] means whether s[i:] can be segmented. Result at dp[0]
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # Empty string is valid

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if s[i : i + len(w)] in wordDict and i + len(w) <= len(s):
                    # We know result of DP[i] based on substring that is later in string
                    # For word neetcode, we know 
                    dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
        return dp[0]