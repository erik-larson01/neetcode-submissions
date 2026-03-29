class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = best = r = 0
        count = defaultdict(int)
        for r in range(len(s)):
            # The max freq char should replace all other chars in the subtstring
            count[s[r]] += 1

            # Every substring must be able to have k replacements
            substrLength = r - l + 1
            if substrLength - max(count.values()) <= k:
                best = max(best, substrLength)
            else:
                count[s[l]] -= 1
                l += 1
        return best