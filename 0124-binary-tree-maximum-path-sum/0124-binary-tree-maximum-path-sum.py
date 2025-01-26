# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Helper function to get the max gain from a node
        def get_max_gain(node):
            # Base case when the node is a leaf
            if not node: return 0

            gain_left = max(get_max_gain(node.left), 0)
            gain_right = max(get_max_gain(node.right), 0)

            curr_max_path = node.val + gain_left + gain_right

            self.max_path = max(self.max_path, curr_max_path)

            return node.val + max(gain_left, gain_right)
        
        # Set max path to negative infinity
        self.max_path = float("-inf")
        get_max_gain(root)

        return self.max_path