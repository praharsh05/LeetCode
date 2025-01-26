# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root: return []

        # BFS approach
        # Variable to keep track of average in a level
        res = []

        q = deque([root])

        while q:
            # Variable to keep track of all the nodes in a level
            n = len(q)
            # Variable to keep track of sum of the val of the nodes in that level
            sum_nodes = 0
            # Iterate over the queue
            for i in range(n):
                node = q.popleft()
                sum_nodes += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                # if we reach the last node average the val and store in res
                if i == n - 1: res.append(sum_nodes/n)
        
        return res
