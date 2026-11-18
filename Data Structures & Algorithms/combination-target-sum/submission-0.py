class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path, current_sum):
            # Base case 1: Exact match found
            if current_sum == target:
                res.append(list(path))
                return
            # Base case 2: Overshot the target, prune branch
            if current_sum > target:
                return
                
            for i in range(start, len(nums)):
                path.append(nums[i])                    # Choose
                backtrack(i, path, current_sum + nums[i]) # Explore (notice 'i', not 'i+1' for reuse)
                path.pop()                                    # Un-choose
                
        backtrack(0, [], 0)
        return res