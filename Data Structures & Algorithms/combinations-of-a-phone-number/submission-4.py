class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(currentStr, i):
            if len(currentStr) == len(digits):
                res.append("".join(currentStr.copy()))
                return
            letters = digitToChar[digits[i]]
            for letter in letters:
                currentStr.append(letter)
                backtrack(currentStr, i + 1)
                currentStr.pop()
        if not digits:
            return []
        backtrack([], 0)
        return res