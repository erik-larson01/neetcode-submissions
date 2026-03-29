class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p,s in zip(position,speed):
            pair.append((p,s))

        pair.sort(reverse=True)
        stack = []
        
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            
            # If time of car farther away <= time of car in front, it will catch up
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)