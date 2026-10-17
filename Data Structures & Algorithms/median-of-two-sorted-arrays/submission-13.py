class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if n < m:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        lo = 0
        hi = m

        while lo <= hi:
            i = lo + (hi - lo)//2
            j = (m+n)//2 - i

            A_left = float("-inf") if i == 0 else nums1[i-1]
            A_right = float("inf") if i == m else nums1[i]
            B_left = float("-inf") if j == 0  else nums2[j-1]
            B_right = float("inf") if j == n else nums2[j]
        
            if (A_left <= B_right) and (B_left <= A_right):
                if (m+n) % 2 == 0:
                    return (min(A_right, B_right) + max(A_left, B_left))/2
                else:
                    return min(A_right, B_right)
            
            if A_left > B_right:
                hi = i - 1
            else:
                lo = i + 1

        

