class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to either min heap and max heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Rebalance (median is the top of either heap)
        # If one heap is larger than the other by more than 1, move top element to other heap
        if len(self.small) - len(self.large) >= 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) - len(self.small) >= 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If sizes differ (odd total elements) return top of larger heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]

        # Sizes are even - return mean of two tops
        return (-1 * self.small[0] + self.large[0]) / 2.0