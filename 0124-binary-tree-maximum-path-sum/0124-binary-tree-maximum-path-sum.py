# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Set max path to negative infinity
        max_path = float("-inf")

        # Helper function to get the max gain from a node
        def get_max_gain(node):
            nonlocal max_path
            # Base case when the node is a leaf
            if not node: return 0

            gain_left = max(get_max_gain(node.left), 0)
            gain_right = max(get_max_gain(node.right), 0)

            curr_max_path = node.val + gain_left + gain_right

            max_path = max(max_path, curr_max_path)

            return node.val + max(gain_left, gain_right)
        
        get_max_gain(root)

        return max_path