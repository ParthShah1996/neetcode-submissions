class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix, answer = [1] * n, [1] * n, [1] * n
        for i in range(len(nums)):
            if i == 0: 
                prefix[i] = 1
            else:
                prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums)-1:
                postfix[j] = 1
            else:
                postfix[j] = postfix[j+1] * nums[j+1]
            
            answer[j] = prefix[j] * postfix[j]

        return answer

            
            
