# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque([root])

        res = []
        direction = True

        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if not direction:
                level.reverse()
            
            res.append(level)
            direction =  not direction
        
        return res