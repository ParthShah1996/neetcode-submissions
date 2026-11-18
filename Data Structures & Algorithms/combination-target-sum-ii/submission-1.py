class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start, path, current_sum):
            # Base case 1: Exact match found
            if current_sum == target:
                res.append(list(path))
                return
            # Base case 2: Overshot the target, prune branch
            if current_sum > target:
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]: 
                    continue
                path.append(candidates[i])                    # Choose
                backtrack(i+1, path, current_sum + candidates[i]) # Explore (notice 'i+1', not 'i' for duplicates)
                path.pop()                                    # Un-choose
                
        backtrack(0, [], 0)
        return res