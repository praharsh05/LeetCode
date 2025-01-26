# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        # BFS approach
        q = deque([root])
        res = []
        while q:
            # Variable to keep track of the nodes in queue
            n = len(q)
            # Iterate over the queue
            for i in range(n):
                node = q.popleft()
                # If the node is last node in the que then it is the rightmost node
                if i == n - 1:
                    res.append(node.val)
                # Add the left and right element of the node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return res