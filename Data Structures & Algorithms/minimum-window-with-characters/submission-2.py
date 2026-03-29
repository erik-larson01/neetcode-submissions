class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = defaultdict(int)
        for c in t:
            freqT[c] += 1

        # Index of window start and end
        best = [-1, -1]
        bestLength = float("infinity")

        freqS = defaultdict(int)
        l = r = 0
        matchedChars = 0
        for r in range(len(s)):
            char = s[r]
            freqS[char] += 1
            if char in freqT and freqT[char] == freqS[char]:
                matchedChars += 1
            
            # Try to find best window 
            while matchedChars == len(freqT):
                # Update best
                if r - l + 1 < bestLength:
                    best = [l,r]
                    bestLength = r - l + 1
                
                # Shrink window
                freqS[s[l]] -= 1

                # Update matchedChars if needed
                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    matchedChars -= 1
                l += 1
        return s[best[0] : best[1] + 1] if bestLength != float("infinity") else ""
