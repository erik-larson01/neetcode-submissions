class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative = [-n for n in nums]
        heapq.heapify(negative)
        # Remove values until the k - 1 largest is the top
        while k > 1:
            # Remove the largest (negative) element
            heapq.heappop(negative)
            k -= 1
        return -negative[0]
