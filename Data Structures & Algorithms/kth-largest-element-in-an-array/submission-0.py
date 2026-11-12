import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [-n for n in nums]
        heapq.heapify(min_heap)
        i = 1
        while min_heap:
            res = heapq.heappop(min_heap)
            if  i == k:
                return -res
            
            i += 1