import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # 1. Turn the list into a standard min heap in O(n) time
        heapq.heapify(self.nums)
        
        # 2. Remove the smallest elements until only the k largest remain
        while len(self.nums) > k:
            heapq.heappop(self.nums)


    def add(self, val: int) -> int:
        # 1. Push the new value into the min heap
        heapq.heappush(self.nums, val)
        
        # 2. If the heap exceeds size k, pop the smallest element
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
            
        # 3. The root of a size-k min heap is always the k-th largest element
        return self.nums[0]


        
    

