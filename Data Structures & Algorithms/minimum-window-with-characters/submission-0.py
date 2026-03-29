class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = defaultdict(int)
        freqS = defaultdict(int)
        l = r = 0

        for c in t:
            freqT[c] += 1
        
        # Holds l, r indices of best window
        best = [-1,-1]
        bestLength = float("infinity")

        matchedCount = 0
        for r in range(len(s)):
            char = s[r]
            freqS[char] += 1
        
            if char in freqT and freqS[char] == freqT[char]:
                matchedCount += 1
            
            while matchedCount == len(freqT):
                if r - l + 1 < bestLength:
                    best = [l, r]
                    bestLength = r - l + 1

                freqS[s[l]] -= 1
                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    matchedCount -= 1
                l += 1
        return s[best[0] : best[1] + 1] if bestLength != float("infinity") else ""