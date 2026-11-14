# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Count length and build a reversed copy of the list
        n = 0
        curr = head
        rev_head = None
        
        while curr:
            new_node = ListNode(curr.val)
            new_node.next = rev_head
            rev_head = new_node
            curr = curr.next
            n += 1
            
        # Step 2: Interleave using i % 2 == 0 up to length n - 1
        p1, p2 = head, rev_head
        for i in range(n - 1):
            if i % 2 == 0:
                tmp = p1.next
                p1.next = p2
                p1 = tmp
            else:
                tmp = p2.next
                p2.next = p1
                p2 = tmp
                
        # Step 3: Cut off the final node's next pointer to prevent a cycle
        if (n - 1) % 2 == 0:
            p1.next = None
        else:
            p2.next = None
