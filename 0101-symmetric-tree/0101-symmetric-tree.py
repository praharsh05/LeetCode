# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Using recursion

        # Helper method to find if two nodes are mirror of each other
        def is_mirror(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        
        return is_mirror(root.left, root.right)