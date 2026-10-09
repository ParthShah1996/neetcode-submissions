class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_length = len(heights)
        indices = []
        best = 0
                
        for i in range(heights_length):
            while indices and heights[indices[-1]] > heights[i]:
                j = indices.pop()
                if not indices:
                    best = max(best , heights[j] * i)
                else:    
                    best = max(best, heights[j] * (i - indices[-1] - 1))
            indices.append(i)
                    
        if indices:
            for i in indices:
                while indices and heights[indices[-1]] >= heights[i]:
                    j = indices.pop()
                    if not indices:
                        best = max(best , heights[j] * heights_length)
                    else:    
                        best = max(best, heights[j] * (heights_length - indices[-1] - 1))
        return best