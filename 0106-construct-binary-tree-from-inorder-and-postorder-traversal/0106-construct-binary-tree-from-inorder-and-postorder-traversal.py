# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder: return
        # last elem of postorder is the root
        root = TreeNode(postorder.pop())

        # Find the index of the root in inorder
        inorder_idx = inorder.index(root.val)

        # Recursively build the right and left subtrees
        root.right = self.buildTree(inorder[inorder_idx + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_idx], postorder)

        return root