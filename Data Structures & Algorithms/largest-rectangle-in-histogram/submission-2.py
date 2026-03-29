class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Increasing height order

        for i, h in enumerate(heights):
            start = i

            # While top of stack is greater than height extend backwards
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index # New bar can start from here
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea