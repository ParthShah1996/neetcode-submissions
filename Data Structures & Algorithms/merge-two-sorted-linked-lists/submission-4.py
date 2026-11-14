# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        res = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                nxt = list1.next
                dummy.next = list1
                dummy = dummy.next
                list1 = nxt
            else:
                nxt = list2.next
                dummy.next = list2
                dummy = dummy.next
                list2 = nxt
        dummy.next = list1 or list2

        return res.next
            

        
        

