# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
           # Grab values if the nodes exist, otherwise treat them as 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add them up along with any carry from the previous step
            total = val1 + val2 + carry
            carry = total // 10         # New carry for the next step
            new_digit = total % 10      # The digit to store in the current node

            # Attach a new node to our result chain
            curr.next = ListNode(new_digit)
            
            # Advance all pointers
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


        