class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = r = 0
        freqS1 = [0] * 26
        freqS2 = [0] * 26
        # Count frequencies of s1 
        for c in s1:
            freqS1[ord(c) - ord("a")] += 1
        
        for r in range(len(s2)):
            # Add char to window
            freqS2[ord(s2[r]) - ord("a")] += 1
            
            # Check window size
            if r - l + 1 > len(s1):
                # Shrink window
                indexOfLast = ord(s2[l]) - ord("a")
                freqS2[indexOfLast] -= 1
                l += 1

            # If both freq match, there is a permutation
            if freqS1 == freqS2: return True
        return False