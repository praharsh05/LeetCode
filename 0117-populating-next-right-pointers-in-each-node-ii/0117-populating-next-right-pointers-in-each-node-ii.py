"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        # BFS approach
        queue = deque()
        queue.append(root)
        # Initialise a dummy node with not null prev
        dummy = Node(-999)
        while queue:
            prev = dummy
            for _ in range(len(queue)):
                visited = queue.popleft()
                if visited.left:
                    queue.append(visited.left)
                    prev.next = visited.left
                    prev = prev.next
                if visited.right:
                    queue.append(visited.right)
                    prev.next = visited.right
                    prev = prev.next
        
        return root
            