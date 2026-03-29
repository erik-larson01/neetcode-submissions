class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_words = defaultdict(list) # char freq -> words

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            freq_words[tuple(count)].append(s)
        return list(freq_words.values())

