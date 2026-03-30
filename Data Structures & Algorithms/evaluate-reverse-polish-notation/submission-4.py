class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # If add, use last 2 values
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # The most recent value is the value to subtract
                minusVal = stack.pop()
                baseVal = stack.pop()
                stack.append(baseVal - minusVal)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # The most recent value in the stack is the divisor
                divisor = stack.pop()
                dividend = stack.pop()
                stack.append(int(float(dividend / divisor)))
            else:
                stack.append(int(token))
        return stack[0]
