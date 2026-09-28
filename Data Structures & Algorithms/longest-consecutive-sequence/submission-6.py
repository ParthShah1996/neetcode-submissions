class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 0
        
        for n in nums_set:
            current_num = n
            current_streak = 1
            
            # Check if the next consecutive number exists in the array
            if n-1 not in nums_set: 
                while (current_num + 1) in nums_set:
                    current_num += 1
                    current_streak += 1
                
            longest = max(longest, current_streak)
            
        return longest