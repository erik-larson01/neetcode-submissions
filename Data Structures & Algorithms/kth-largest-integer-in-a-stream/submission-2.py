class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initalize using a heap of size k
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # Push to the heap, then if the size > k, pop largest
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]