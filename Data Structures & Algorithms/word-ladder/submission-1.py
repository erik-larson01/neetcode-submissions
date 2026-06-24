class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Shortest path in unweighted graph where words = nodes
        # And edges connect words that differ by one char
        words = set(wordList)
        res = 0
        q = deque([beginWord])

        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for i in range(len(node)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == node[i]:
                            continue
                        neighbor = node[:i] + c + node[i + 1:]
                        if neighbor in words:
                            q.append(neighbor)
                            words.remove(neighbor)
        return 0
