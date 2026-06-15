class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        # Build adjacency list
        adjList = [[] for i in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # Use DFS to find all nodes visited in a connected component
        def dfs(node):
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Every time we dfs from a new unvisited node, that is a new component
        for node in range(n):
            if node not in visited:
                visited.add(node)
                res += 1
                dfs(node)

        return res