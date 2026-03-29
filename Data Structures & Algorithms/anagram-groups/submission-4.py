from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for initial_word in strs:
            # Sort word into a list then back into a string
            sorted_word = "".join(sorted(initial_word))
            result[sorted_word].append(initial_word)
        
        return list(result.values())
