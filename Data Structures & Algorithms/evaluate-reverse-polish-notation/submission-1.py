class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # For every operator, pop the last two values
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(float(val2 / val1)))
            else:
                # Not an operator
                stack.append(int(token))
        return stack[0]