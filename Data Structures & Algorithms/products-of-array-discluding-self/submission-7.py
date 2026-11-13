class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n_len = len(nums)
        res = [1] * n_len

        # Store prefix products directly in res
        for i in range(1, n_len):
            res[i] = nums[i - 1] * res[i - 1]

        # Track postfix product with a single variable
        postfix = 1
        for i in range(n_len - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res





        