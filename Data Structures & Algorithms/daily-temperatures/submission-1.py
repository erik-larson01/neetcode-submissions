class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Temp, Index
        result = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            # Check if new temp > vals in stack
            while stack and temp > stack[-1][0]:
                # Remove val
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            # Add val to stack
            stack.append((temp, i))
        return result