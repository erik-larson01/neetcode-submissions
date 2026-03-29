class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            # Remove smaller values from queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Add index r to top of queue
            q.append(r)

            # Check if top val in queue is out of left bound
            if l > q[0]:
                q.popleft()
            
            # Check size of queue is k (0 based indexing, add 1)
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output