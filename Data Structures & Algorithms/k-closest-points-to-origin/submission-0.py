class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use min-heap of size k
        distHeap = []
        for x, y in points:
            # Compare distance to the origin
            dist = math.sqrt(x**2 + y**2)
            distHeap.append((dist, x, y))
            print(f"Dist: {dist} for point {x}, {y}")
        # Heapify will sort based on first value of tuple, so distance
        heapq.heapify(distHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(distHeap)
            res.append([x,y])
            k -= 1
        return res