class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Temp, Index
        result = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((temp, i))
        return result