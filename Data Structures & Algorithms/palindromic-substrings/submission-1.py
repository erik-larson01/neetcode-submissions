class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # Check every char to see if middle of palindrome
        for i in range(len(s)):
            # Odd length palindrome
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            
            # Even length palindrome
            l = i
            r = i + 1 # Adjacent index
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res