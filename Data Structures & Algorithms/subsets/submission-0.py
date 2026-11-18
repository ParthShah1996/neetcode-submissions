class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            # Create new subsets by adding the current number to all existing subsets
            res += [curr + [num] for curr in res]
        return res