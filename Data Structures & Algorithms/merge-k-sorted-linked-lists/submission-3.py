# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        min_heap = [] # Initialize an empty heap list
        counter = 0 # Counter for every node to break tiebreaks
        
        for l in lists:
            # Push head of each list, counter for tiebreaks, node itself to min_heap
            if l:
                heapq.heappush(min_heap, (l.val, counter, l))
                counter += 1

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val,_, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next
            
