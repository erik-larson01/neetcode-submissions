from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        result = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            words[sorted_word].append(word)
        
        for anagram in words:
            result.append(words[anagram])
        return result
