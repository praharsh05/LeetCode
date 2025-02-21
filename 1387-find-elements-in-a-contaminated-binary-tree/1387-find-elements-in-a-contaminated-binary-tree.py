# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def recover(self, root):
        if root and root.val == -1: root.val = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                node.left.val = 2* node.val + 1
                stack.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                stack.append(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.recover(self.root)
    
    
    def find(self, target: int) -> bool:
        if not self.root: return False
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.val == target: return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)