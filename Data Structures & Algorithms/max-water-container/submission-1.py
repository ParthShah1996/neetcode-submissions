class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        i = 0
        j = length - 1
        area = 0
        while i < j:
            hi = heights[i]
            hj = heights[j]
            area = max((j - i) *min(hi,hj), area)
            if hi < hj:
                i += 1
            else:
                j -= 1
        return area