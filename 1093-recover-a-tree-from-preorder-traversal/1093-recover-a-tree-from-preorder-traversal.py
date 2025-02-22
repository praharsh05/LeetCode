# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.idx = 0
        self.level = 0
        node = TreeNode(-1)

        def helper(parent, level):
            while self.idx < len(traversal) and level == self.level:
                num = 0
                while self.idx < len(traversal) and traversal[self.idx].isdigit():
                    num = num * 10 + int(traversal[self.idx])
                    self.idx += 1
                node = TreeNode(num)

                if not parent.left:
                    parent.left = node
                else:
                    parent.right= node
                
                self.level = 0
                while self.idx < len(traversal) and traversal[self.idx] == "-":
                    self.level += 1
                    self.idx += 1
                helper(node, level+1)
        
        helper(node, 0)
        return node.left