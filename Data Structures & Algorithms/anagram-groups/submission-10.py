class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Freq -> Strings
        freq_map = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            freq_map[tuple(freq)].append(s)
        return list(freq_map.values())
