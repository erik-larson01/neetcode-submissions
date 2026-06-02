class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}': '{', ')': '(', ']': '['}
        stack = []
        for bracket in s:
            if bracket in closeToOpen:
                # If closing bracket, try to pop 
                if stack and stack[-1] == closeToOpen[bracket]:
                    # Brackets match
                    stack.pop()
                else:
                    # Brackets do not match, Fail
                    return False
            else: # Opening tag
                stack.append(bracket)
            
        return True if not stack else False