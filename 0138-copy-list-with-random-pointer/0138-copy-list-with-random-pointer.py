"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Use hash table
        hash = {None:None}
        res = head

        while res:
            hash[res] = Node(res.val)
            res = res.next
        
        res = head

        while res:
            copy = hash[res]
            copy.next = hash[res.next]
            copy.random = hash[res.random]
            res = res.next
        
        return hash[head]