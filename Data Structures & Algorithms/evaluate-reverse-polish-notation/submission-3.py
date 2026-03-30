class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                minusVal = stack.pop()
                baseVal = stack.pop()
                stack.append(baseVal - minusVal)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                divisor = stack.pop()
                dividend = stack.pop()
                stack.append(int(float(dividend / divisor)))
            else:
                stack.append(int(token))
        return stack[0]
