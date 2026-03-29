class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #Map char count to list of anagrams
        for string in strs:
            count = {}
            for char in string:
                count[char] = count.get(char, 0) + 1
            result[tuple(sorted(count.items()))].append(string)
        return list(result.values())


