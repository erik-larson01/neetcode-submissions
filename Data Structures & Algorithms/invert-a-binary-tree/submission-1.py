# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use DFS or BFS and swap the children
        if not root:
            return None
        
        # Swap children
        root.left, root.right = root.right, root.left

        # Continue this process recursively on both subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root