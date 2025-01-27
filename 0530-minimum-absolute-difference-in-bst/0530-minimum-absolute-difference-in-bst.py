# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        min_diff = float("inf")
        
        curr = root
        prev = -10**5
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            min_diff = min(min_diff, node.val - prev)
            prev = node.val
            curr = node.right
        
        return min_diff

        