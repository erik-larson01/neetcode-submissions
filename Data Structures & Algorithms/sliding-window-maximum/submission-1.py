class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # Stores INDICES of elements in decreasing order
        queue = deque()
        l = r = 0
        while r < len(nums):
            # Remove smaller values (will never be max)
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if r + 1 >= k:
                # Append val at index of the front of queue
                output.append(nums[queue[0]])
                l += 1
            r += 1
        return output

