# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = None

        slow = head
        fast = head

        length = 0
        while fast and fast.next:
            length += 2
            fast = fast.next.next
            slow = slow.next

        if fast:
            length += 1

        pos = length - n
        i = 0
        curr = head
        
        while curr:
            if i == pos == 0:
                head = head.next
                curr = curr.next

            elif i == pos-1:
                if curr.next:
                    nxt = curr.next.next
                    curr.next = curr.next.next
                    curr = nxt
                else:
                    curr.next = None
                    curr = None
            else:
                curr = curr.next
            i += 1
        return head