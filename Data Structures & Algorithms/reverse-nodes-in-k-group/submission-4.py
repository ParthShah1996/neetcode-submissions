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

        parts_reversed = length//k # Only reverse length//k times k parts of linked list head
        
        start = ListNode(1) # Dummy node to return the result.
        start.next = head # If k > length returns head directly.
        tag = start # Another tag to keep track of the last node in a group.
        prev = None # To store the previous node in the loop. 
        curr = head # To store the current node in the loop.

        for i in range(0, parts_reversed):
            for i in range(k):
                if i == 0:
                    tail = curr
                nxt = curr.next # Store the next node to be reversed.
                curr.next = prev # Change the arrow of the curr node to previous node / None
                prev = curr # Assign prev to curr, for the next iteration.
                curr = nxt # Move to the next node to be reversed.
                
            tag.next = prev # Join the reversed group to the result
            tag = tail # Reposition to element before the next group to join the next reversed group
            prev = None # Reset prev to None to reverse next group
            tail.next = curr  # Attach the next nodes if they are not reversed.
        
        return start.next