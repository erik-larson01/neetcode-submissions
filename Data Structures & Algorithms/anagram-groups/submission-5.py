class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Key: frequencies of every letter, Val: anagram

        for s in strs:
            count = [0] * 26
            for c in s:
                # Use ord (ordinal) to have "a" be at index 0 of count
                count[ord(c) - ord("a")] += 1
            # Lists cannot be keys, turn into tuples
            result[tuple(count)].append(s)

        return list(result.values())
            