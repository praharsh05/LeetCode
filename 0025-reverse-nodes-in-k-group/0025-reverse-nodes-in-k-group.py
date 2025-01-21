# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Helper function to reverse k nodes in a linked list
    def reverse_list(self, head: Optional[ListNode], k: int):
        
        prev = None
        curr = head

        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev, curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy

        while ptr is not None:
            tracker = ptr

            # Check if there are k nodes to reverse
            for _ in range(k):
                tracker = tracker.next
                # If fewer than k nodes then return the original
                if tracker is None:
                    return dummy.next
            
            # Reverse k nodes
            prev, curr = self.reverse_list(ptr.next, k)

            last_node_of_reversed_group = ptr.next
            last_node_of_reversed_group.next = curr
            ptr.next = prev
            
            ptr = last_node_of_reversed_group # Move ptr forward
        
        return dummy.next
    
    