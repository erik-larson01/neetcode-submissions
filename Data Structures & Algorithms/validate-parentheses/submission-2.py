class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { "(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                # Process closing tag
                if not stack:
                    return False
                elif pairs[stack[-1]] != c:
                    print(c)
                    return False
                else:
                    stack.pop()
        return True if not stack else False
