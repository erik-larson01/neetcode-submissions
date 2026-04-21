class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distHeap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            distHeap.append((dist, x, y))
        heapq.heapify(distHeap)
        res = []
        while k > 0:
            k -= 1
            dist, x, y = heapq.heappop(distHeap)
            res.append([x, y])
        return res
