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
        step = {}                 # phone book: old node -> new node
        head2 = head              # keep a tag on the original head
        copyList = Node(0)
        dummy = copyList

        # Loop 1: make copies, link next, fill the phone book
        while head:
            nxt = Node(0)
            nxt.val = head.val
            copyList.next = nxt
            copyList = copyList.next
            step[head] = nxt
            head = head.next

        # Loop 2: set random using the phone book
        while head2:
            if head2.random:
                step[head2].random = step[head2.random]
            else:
                step[head2].random = None
            head2 = head2.next

        return dummy.next