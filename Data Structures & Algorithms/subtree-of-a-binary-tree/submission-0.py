# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases
        if not root:
            return False
        if not subRoot:
            return True
        
        # DFS with root and subroot (check if both are the same tree)
        if self.sameTree(root, subRoot):
            return True
        # Recursively try again with left and right children
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))

    def sameTree(self, root1, root2):
            # Same functionality as "Same Binary Tree"
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)