class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]

        # Sort cars by descending order, so we look at closest first
        pairs.sort(reverse=True)
        numFleets = 1
        # Track time of closest to target
        prevTime = (target - pairs[0][0]) / pairs[0][1]

        for p,s in pairs:
            time = (target - p) / s

            # If time > prevTime, car cannot catch up and will form a new fleet
            if time > prevTime:
                numFleets += 1
                prevTime = time
        return numFleets