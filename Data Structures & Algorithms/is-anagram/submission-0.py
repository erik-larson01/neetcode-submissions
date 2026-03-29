class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        total_s = {}
        total_t = {}
        for letter in s:
            if letter not in total_s:
                total_s[letter] = 1
            else:
                total_s[letter] = total_s[letter] + 1
            
        for letter in t:
            if letter not in total_t:
                total_t[letter] = 1
            else:
                total_t[letter] = total_t[letter] + 1

        if total_t != total_s:
            return False
        return True
