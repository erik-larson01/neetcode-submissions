class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove spaces and capital letters
        s = "".join(s.split(" ")).lower()

        # Remove non alphanumeric chars
        s = "".join(filter(str.isalnum, s))
        
        l,r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True