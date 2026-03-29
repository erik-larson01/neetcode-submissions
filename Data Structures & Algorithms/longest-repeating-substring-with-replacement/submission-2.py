class Solution:
    def characterReplacement(self, s: str, k: int) -> int:     
        best = 0   
        for i in range(len(s)):
            freq = defaultdict(int)
            for j in range(i, len(s)):
                freq[s[j]] += 1

                # (j - i + 1 is len of substring)
                if (j - i + 1) - max(freq.values()) <= k: # number of replacements
                    best = max(best, j - i + 1)
        return best