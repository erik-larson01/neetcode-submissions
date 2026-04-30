class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currentList = [] # currentList of chosen palindromes

        # Explore all valid ways to cut string s
        def dfs(i):
            if i >= len(s):
                res.append(currentList.copy())
                return
            # At every starting index, find where to partition next
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    # Keep only palindromes and backtrack
                    currentList.append(s[i : j + 1])
                    dfs(j + 1)
                    currentList.pop()
        dfs(0)
        return res

    # Palindrome verification 
    def isPalindrome(self, string, l, r):
        while l < r:
            if string[l] != string[r]:
                return False
            l,r = l + 1, r - 1
        return True