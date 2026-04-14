# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                # If we see a null node append Null as a string
                res.append("Null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res) # Use a , as a delimiter
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Turn the encoded data into a queue
        values = deque(data.split(","))
        
        def dfs(values):
            # Retrieve value via popleft
            val = values.popleft()

            # Return None if value is "Null"
            if val == "Null":
                return None

            # Create a node
            node = TreeNode(int(val))

            # Build left and right subtrees
            node.left = dfs(values)
            node.right = dfs(values)

            return node
        return dfs(values)