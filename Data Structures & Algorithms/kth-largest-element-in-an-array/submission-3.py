class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq only does min heap, so we make all values negative
        negative = [-num for num in nums]
        heapq.heapify(negative)

        while k > 1:
            k -= 1
            heapq.heappop(negative)
        return -1 * negative[0]