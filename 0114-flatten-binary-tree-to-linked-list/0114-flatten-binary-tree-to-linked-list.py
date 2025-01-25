# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Pointer to traverse the tree
        curr = root

        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Connect the right subtree to the right of prev
                prev.right = curr.right
                # Move the left subtree to the right and set left to null
                curr.right = curr.left
                curr.left = None
            
            # Move to the right
            curr = curr.right