class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        # DFS to "fill" all of a connected component
        def dfs(node):
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)

            return False
        
        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
        return components
        