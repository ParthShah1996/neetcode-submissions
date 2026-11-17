class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left =  0
        right = len(nums) - 1

        while left <= right:
            mid_point = left + (right - left) // 2  
            if nums[mid_point] == target:
                return mid_point

            if target > nums[mid_point] :
                left = mid_point + 1
            else:
                right = mid_point - 1

        return -1


        
