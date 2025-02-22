# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # New List with head set to the start
        new_list = ListNode()
        # result list 
        res = new_list

        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            
            res = res.next
        # if any element left in the lists
        if list1:
            res.next = list1
        else:
            res.next = list2
        
        return new_list.next
