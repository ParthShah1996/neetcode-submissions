class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path):
            # Base case: if our path is the same length as nums, we found a full permutation
            if len(path) == len(nums):
                res.append(list(path))
                return
                
            for num in nums:
                # Skip numbers already used in the current path
                if num in path:
                    continue
                    
                path.append(num)        # Choose
                backtrack(path)         # Explore
                path.pop()              # Un-choose (Backtrack)
                
        backtrack([])
        return res