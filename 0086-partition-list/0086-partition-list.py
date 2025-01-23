# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two linked list to store values smaller and lager
        slist, blist = ListNode(), ListNode()
        # Two pointers for both the lists
        small, big = slist, blist

        # Traverse the list
        while head:
            # If val is lower than x add it to slist
            if head.val < x:
                small.next = head
                small = small.next
            # Else add it to blist
            else:
                big.next = head
                big = big.next
            
            head = head.next
        
        # connect the tail of slist with the head of blist
        small.next = blist.next
        # Set the tail of blist to null
        big.next = None

        return slist.next