class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}

        # Use dictionaries to check values of every letter because order does not matter
        for letter in s:
            if letter not in s_letters:
                s_letters[letter] = 0
            s_letters[letter] += 1
        
        for letter in t:
            if letter not in t_letters:
                t_letters[letter] = 0
            t_letters[letter] += 1
        
        print(s_letters)
        print(t_letters)

        return s_letters == t_letters