class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        res = 0
        while l < r:
            # Find amount of water
            water = (r - l) * min(heights[l], heights[r])
            res = max(res, water)

            # Adjust pointers based on min height (water cannot exceed)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                # If equal, either inc or dec works (could add <= or >= above)
                l += 1
        return res