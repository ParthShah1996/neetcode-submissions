class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] # Stores max element for each step
        q = deque()
        nums_length = len(nums)
        nums_map = {}

        for i in range(nums_length):
            if q and q[0] < i - k + 1: # Current window
                q.popleft()
            
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            if i >= k - 1:
                res.append(nums[q[0]])
        return res