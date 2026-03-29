class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, r, best = -1, 0, 0

        for r in range(len(s)):
            char = s[r]
            if char in window:
                # Shrink window
                while char in window:
                    l += 1
                    removedVal = s[l]
                    window.remove(removedVal)
            window.add(char)
            best = max(best, len(window))
        return best