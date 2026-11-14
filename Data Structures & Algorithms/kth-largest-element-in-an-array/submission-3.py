import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Keep a min-heap of size at most k
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap) # Pop the smallest, keeping only the top k largest
                
        # The root of the min-heap is now the k-th largest element
        return min_heap[0]