class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stone values to negative to use min_heap 
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)
            if secondStone > firstStone:
                heapq.heappush(stones, firstStone - secondStone)
        stones.append(0)
        return abs(stones[0])