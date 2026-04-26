class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(openNum, closedNum):
            if openNum == closedNum == n:
                # Valid parenthesis, save to res
                res.append("".join(stack))
                return
            
            if openNum < n:
                # A "(" can be added
                stack.append("(")
                backtrack(openNum + 1, closedNum)
                stack.pop()
            if closedNum < openNum: # Parentheses need to be completed
                # A ")" can be added
                stack.append(")")
                backtrack(openNum, closedNum + 1)
                stack.pop()

        backtrack(0,0)
        return res    