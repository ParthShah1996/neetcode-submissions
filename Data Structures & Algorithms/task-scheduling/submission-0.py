import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequencies
        count = Counter(tasks)
        
        # Build max-heap of frequencies
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque() # Stores pairs of [cnt, available_time]
        
        while max_heap or q:
            time += 1
            
            if max_heap:
                cnt = heapq.heappop(max_heap)
                # Since cnt is negative, incrementing it brings it closer to 0
                cnt += 1 
                if cnt != 0:
                    q.append([cnt, time + n])
            
            # Check if any task on cooldown is now ready to re-enter the heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
                
        return time