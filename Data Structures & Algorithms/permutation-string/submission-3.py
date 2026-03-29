class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n + m) time
        freq1 = [0] * 26
        freq2 = [0] * 26
        l = r = 0

        # Get frequency count of s1
        for num in s1:
            freq1[ord(num) - ord("a")] += 1

        for r in range(len(s2)):
            freq2[ord(s2[r]) - ord("a")] += 1
            
            if r - l + 1 > len(s1):
                indexOfLast = ord(s2[l]) - ord("a")
                freq2[indexOfLast] -= 1
                l += 1

            if freq1 == freq2:
                return True

        return False