# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Slow and Fast runner approach
        slow = fast = head

        while fast and fast.next:
            # Move slow by 1 and fast by 2
            slow = slow.next
            fast = fast.next.next

            # If fast catches up to slow then there is a cycle
            if slow == fast:
                return True
        
        return False