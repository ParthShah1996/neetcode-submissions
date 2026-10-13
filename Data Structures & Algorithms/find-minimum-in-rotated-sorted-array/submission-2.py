class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        # If the there is no rotation or n rotations our min value is nums[0]

        while start <= end:
            
            mid = start + (end - start)//2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
                
        min_value = nums[end]
        return min_value
