class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Increasing height order

        for i, h in enumerate(heights):
            start = i

            # While top of stack is greater than height of bar i
            while stack and stack[-1][1] > h:
                # New bar is shorter than top of stack. Taller bar cannot extend to the right.
                index, height = stack.pop()
                # Compute area it could cover
                maxArea = max(maxArea, height * (i - index))
                start = index # New shorter bar can start as far left as popped bars start index
            stack.append((start, h))

        # Process remaining bars in stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea