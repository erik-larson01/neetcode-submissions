"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                # Use that node
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for n in node.neighbors:
                cloned_neighbor = dfs(n)
                copy.neighbors.append(cloned_neighbor)

            return copy

        return dfs(node) if node else None
