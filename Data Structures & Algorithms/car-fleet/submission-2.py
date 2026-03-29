class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]

        pairs.sort(reverse=True)
        numFleets = 1
        prevTime = (target - pairs[0][0]) / pairs[0][1]

        for p,s in pairs:
            time = (target - p) / s

            if time > prevTime:
                numFleets += 1
                prevTime = time
        return numFleets