class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIndex = 0 # Starting index of palindrome

        # Check every char to see if middle of palindrome
        for i in range(len(s)):
            # Odd length palindrome
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If largest palindrome, set new resLen and resIndex
                if (r - l + 1) > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l -= 1
                r += 1
            # Even length palindrome
            l = i
            r = i + 1 # Adjacent index

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l -= 1
                r += 1
        return s[resIndex: resIndex + resLen]