# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find the length of k
        dummy = head
        length = 0
        while dummy:
            dummy = dummy.next
            length += 1

        parts_reversed = length//k
        # Only reverse length//k times k parts of linked list head
        
        start = ListNode(1)
        start.next = head
        tag = start
        prev = None
        curr = head

        for i in range(0, parts_reversed):
            for i in range(k):
                if i == 0:
                    tail = curr
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            tag.next = prev
            tag = tail
            prev = None
            tail.next = curr  # Attach the next nodes if they are not reversed.
        
        return start.next