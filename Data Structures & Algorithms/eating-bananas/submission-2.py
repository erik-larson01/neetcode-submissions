class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        topK = max(piles)
        bottomK = 1
        result = topK

        while bottomK <= topK:
            midK = (bottomK + topK) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / midK)
            if totalTime <= h:
                topK = midK - 1
                result = midK
            else:
                bottomK = midK + 1
        return result