class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = defaultdict(list)
        for s in strs:
            sortedString = sorted(s)
            sortedKey = ''.join(sortedString)
            strDict[sortedKey].append(s)
        return list(strDict.values())
        


