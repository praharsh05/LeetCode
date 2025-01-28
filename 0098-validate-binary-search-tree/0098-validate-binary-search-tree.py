# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(node, min_val, max_val):
            if not node:
                return True  # An empty subtree is valid
            
            if not (min_val < node.val < max_val):
                return False  # Node violates BST rule
            
            # Check left subtree (values must be < node.val)
            # Check right subtree (values must be > node.val)
            return is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)
        
        return is_valid(root, float('-inf'), float('inf'))