class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        visited = set()
        adjList = [[] for i in range(n)]
        
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n