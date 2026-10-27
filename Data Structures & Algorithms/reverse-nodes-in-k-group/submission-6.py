# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Pass 1: count the nodes
        node = head
        length = 0
        while node:
            node = node.next
            length += 1
        groups = length // k           # number of full groups

        start = ListNode(0)            # dummy node before the head
        start.next = head
        tag = start                    # the node before the current group
        prev = None
        curr = head

        for _ in range(groups):
            tail = curr                # first node of the group = tail after reversing
            for _ in range(k):         # Reverse Linked List, k times
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tag.next = prev            # join: node before the group -> new head
            tail.next = curr           # join: new tail -> the rest of the list
            tag = tail                 # now the node before the next group
            prev = None                # fresh start for the next group

        return start.next