class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(len(edges) + 1)]

        # Check if a cycle (True means cycle exists)
        def dfs(node, parent, visited):
            if node in visited:
                return True
            
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node, visited):
                    return True
            return False
            
        # Add edges to the list one at a time
        for u, v in edges:
            visited = set()

            # We need the first edge that returns true/makes a cycle
            adjList[u].append(v)
            adjList[v].append(u)

            # Call DFS on the node itself
            if dfs(u, -1, visited):
                return [u,v]
        return []
