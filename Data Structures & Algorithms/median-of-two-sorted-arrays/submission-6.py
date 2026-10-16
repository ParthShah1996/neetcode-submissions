class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        total_size = m+n
        left_half_items = total_size//2

        for i in range(left_half_items + 1):
            j = left_half_items - i

            if m <= n:
                A_left = float("-inf") if i == 0 else nums1[i-1]
                B_left = float("-inf") if j == 0 else nums2[j-1]
                A_right = float("inf") if i == m else nums1[i]
                B_right = float("inf") if j == n else nums2[j]
            else:
                A_left = float("-inf") if i == 0 else nums2[i-1]
                B_left = float("-inf") if j == 0 else nums1[j-1]
                A_right = float("inf") if i == n else nums2[i]
                B_right = float("inf") if j == m else nums1[j]

            if (A_left <= B_right) and (B_left <= A_right):
                if total_size % 2 == 0:
                    return (min(A_right, B_right) + max(A_left, B_left))/2
                else:
                    return min(A_right, B_right)
            
                
        

