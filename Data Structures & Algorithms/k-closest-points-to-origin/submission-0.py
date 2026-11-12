import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []

        for x, y in points:
            # Use squared distance to avoid sqrt and floating-point issues
            dist_sq = x*x + y*y
            min_heap.append((dist_sq, [x, y]))
            
        heapq.heapify(min_heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        return res