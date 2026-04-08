# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxAlongPath):
            if not node:
                return 0
            
            # A node is good if no earlier node has a value greater than it
            # So, track max val seen so far along the searched path
            goodCount = 0
            if node.val >= maxAlongPath:
                goodCount += 1
                maxAlongPath = node.val

            left = dfs(node.left, maxAlongPath)
            right = dfs(node.right, maxAlongPath)

            # Return good node count of current path + left and right paths
            return left + right + goodCount
        return dfs(root, root.val)