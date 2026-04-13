class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define the range of what k can be
        minK, maxK = 1, max(piles)
        result = maxK

        while minK <= maxK:
            midK = (minK + maxK) // 2
            totalTime = 0
            for pile in piles:
                # Time taken is ceil(x / k) as Koko finishes the full hour
                totalTime += math.ceil(float(pile) / midK)
            if totalTime <= h:
                # Speed works, record it and search left half
                maxK = midK - 1
                result = midK
            else:
                # Speed is too slow, search in right half
                minK = midK + 1

        return result