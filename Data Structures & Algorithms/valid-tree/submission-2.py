class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # A Tree has no cycles and has n - 1 edges
        if len(edges) > n - 1:
            return False

        # Build adjacency List
        adjList = [[] for i in range(n)]
        for u, v in edges:
            # Undirected graph, edges go both ways
            adjList[u].append(v)
            adjList[v].append(u)

        # Use DFS to check if it has a cycle

        visited = set()
        def dfs(node, parent):
            # Check for cycle
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        # All nodes must be visited
        return dfs(0, -1) and len(visited) == n