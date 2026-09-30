class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l<r:
            if leftMax < rightMax:
                l += 1
                heightL = height[l]
                leftMax = max(leftMax, heightL)
                res += leftMax - heightL
            else:
                r -= 1
                heightR = height[r]
                rightMax = max(rightMax,  heightR)
                res += rightMax -  heightR
        return res