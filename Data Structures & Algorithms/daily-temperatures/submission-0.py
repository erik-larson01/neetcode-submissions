class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            greater = 0
            first = False
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    if not first:
                        greater = j - i
                        first = True
            result.append(greater)
        return result