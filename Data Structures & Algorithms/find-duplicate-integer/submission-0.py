class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = {}
        for n in nums:
            if n in duplicate:
                return n                
            duplicate[n] = n

        