"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Use a hashmap to remember what we have already copied
        oldToNew = {}
        def dfs(node):
            # If we already have copied a node, we reuse it
            if node in oldToNew:
                return oldToNew[node]
            
            # Make a copy of the node and add it to the hashmap
            copy = Node(node.val)
            oldToNew[node] = copy

            # Recursively clone all neighbors of the node and add them to the clone neighbors list
            for n in node.neighbors:
                cloned_n = dfs(n)
                copy.neighbors.append(cloned_n)
            return copy
        return dfs(node) if node else None