# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        count = 0
        stack = [root]

        while len(stack) > 0:
            visited = stack.pop()
            count += 1
            if visited.right: stack.append(visited.right)
            if visited.left: stack.append(visited.left)

        return count
