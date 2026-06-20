class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Make adjacency list (numNodes = numEdges + 1)
        adjList = [[] for _ in range(len(edges) + 1)]
        
        # Detect cycle using DFS (True = cycle exists)
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

        for u, v in edges:
            # Add edges to graph THEN call dfs
            # DFS is called now, not after the adjList has been made
            # This is because we need to return the first edge that returns a cycle
            adjList[u].append(v)
            adjList[v].append(u)

            # Reinitialize the set every time to reset what has been visited
            visited = set()

            if dfs(u, -1, visited):
                return [u,v]
        # No redundant edge found
        return []
            