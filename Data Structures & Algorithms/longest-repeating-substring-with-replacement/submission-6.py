class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = best = 0
        count = defaultdict(int)

        for r in range(len(s)):
            # Max freq character should be the replacing char
            count[s[r]] += 1

            substringLen = r - l + 1
            # Window - maxFreq is num values that can be replaced
            if substringLen - max(count.values()) <= k:
                # Replace can occur
                best = max(best, substringLen)
            else:
                # Shrink window
                count[s[l]] -= 1
                l += 1
        return best