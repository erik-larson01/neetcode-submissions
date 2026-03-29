class Solution:
    def characterReplacement(self, s: str, k: int) -> int:     
        best = 0   
        for i in range(len(s)):
            freq = defaultdict(int)
            maxFreq = 0
            for j in range(i, len(s)):
                # K chars need to be replaced with maxFreq char
                freq[s[j]] += 1
                maxFreq = max(maxFreq, freq[s[j]])

                # (j - i + 1 is len of substring)
                if (j - i + 1) - maxFreq <= k: # number of replacements
                    best = max(best, j - i + 1)
        return best