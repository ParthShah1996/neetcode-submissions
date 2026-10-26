# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq          # at the top of the file

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        counter = 0                       # tie breaker

        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, counter, l))
                counter += 1

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next