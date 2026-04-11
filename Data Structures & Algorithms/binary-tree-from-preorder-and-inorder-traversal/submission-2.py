# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Val -> Index
        inOrderIndices = {}
        for index, val in enumerate(inorder):
            inOrderIndices[val] = index
        
        # The root is at preorder[0]
        self.rootIndex = 0
        def dfs(left, right):
            if left > right:
                return None
            
            # Get the value of the root by indexing into the preorder array
            rootValue = preorder[self.rootIndex]
            rootNode = TreeNode(rootValue)
            self.rootIndex += 1
            # The middle index is where the root is, which splits the tree
            midIndex = inOrderIndices[rootValue]
            # left
            rootNode.left = dfs(left, midIndex - 1)
            # right
            rootNode.right = dfs(midIndex + 1, right)
            return rootNode
        return dfs(0, len(inorder) - 1)
            

