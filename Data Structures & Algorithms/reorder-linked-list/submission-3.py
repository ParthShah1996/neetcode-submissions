# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # First we try to find the mid point of the list.
        # We can do it running a while loop on a fast pointer moving 2 steps at a time.
        # This will ensure that slow pointer is at the half length mark.

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        # We reverse the second half (starting from slow.next)
        curr = slow.next
        prev = None

        slow.next = None # Seperate the first and second half
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Create two pointers for both the halves
        first = head
        second = prev

        while second: # We do second because second will have always have less nodes.
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2