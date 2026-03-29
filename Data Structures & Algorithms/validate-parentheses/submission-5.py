class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for c in s:
            if c in closeToOpen: # Ending tag
                # Check if top of stack is opening tag
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: # Opening tag
                stack.append(c)
        return True if not stack else False