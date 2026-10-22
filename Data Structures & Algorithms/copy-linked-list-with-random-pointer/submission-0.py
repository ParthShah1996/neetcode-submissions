"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        step = {}
        head2 = head
        copyList = Node(0)
        dummy = copyList
        res = dummy
        while head:        
            nxt = Node(0)
            nxt.val = head.val
            copyList.next = nxt
            copyList = copyList.next
            step[head] = nxt
            head = head.next

        dummy = dummy.next
        while head2:
            if step[head2] and head2.random:
                step[head2].random = step[head2.random]
            else:
                step[head2].random = None
        
            head2 = head2.next
        
        return res.next

