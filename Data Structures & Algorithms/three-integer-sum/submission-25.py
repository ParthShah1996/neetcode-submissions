class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums = sorted(nums)
        output = []      
        
        for k in range(length):
            
            if k > 0 and nums[k] == nums[k-1]:
                continue
            
            i = k + 1
            j = length - 1

            while (i < j):
                numsi = nums[i]
                numsj = nums[j]
                numsk = nums[k]
                current_sum = numsi + numsj + numsk
                if current_sum < 0:
                    i += 1
                elif  current_sum > 0:
                    j -= 1
                else:
                    output.append([numsi,numsj,numsk])
                    i += 1
                    j -= 1
                
                    while (i < j) and nums[i] == nums[i-1]:
                        i += 1

        return output


