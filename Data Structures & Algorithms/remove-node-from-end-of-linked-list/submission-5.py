# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        front = dummy
        back = dummy
        i = 0
        while i < n:
            front = front.next
            i += 1
        while front and front.next:
            front = front.next
            back = back.next
        
        if back.next:
            back.next = back.next.next
        else:
            back = None

        return dummy.next