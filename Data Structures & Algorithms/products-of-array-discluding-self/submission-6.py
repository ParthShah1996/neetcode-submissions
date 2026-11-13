class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        prefix = [1]*n_len
        postfix = [1]*n_len
        res = [1]*n_len

        for i in range(n_len):
            if i == 0:
                continue              
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(n_len - 1, -1, -1):

            if i == n_len - 1:
                res[i] = prefix[i] * postfix[i]

                continue
            postfix[i] = nums[i+1] * postfix[i+1]
            res[i] = prefix[i] * postfix[i]


        return res
        




        