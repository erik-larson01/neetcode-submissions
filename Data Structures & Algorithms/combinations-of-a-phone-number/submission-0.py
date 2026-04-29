class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(currStr, i):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            # Try all possible characters for that digit
            letters = digitToChars[digits[i]]
            for char in letters:
                # Add the character to the current string
                backtrack(currStr + char, i + 1)
        
        if not digits: return []
        backtrack("", 0)
        return res