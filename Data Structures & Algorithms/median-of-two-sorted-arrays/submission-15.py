class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A              # A is always the shorter array
        m, n = len(A), len(B)
        half = (m + n) // 2

        lo, hi = 0, m                # i can be 0 to m
        while lo <= hi:
            i = lo + (hi - lo) // 2
            j = half - i

            A_left = float("-inf") if i == 0 else A[i - 1]
            A_right = float("inf") if i == m else A[i]
            B_left = float("-inf") if j == 0 else B[j - 1]
            B_right = float("inf") if j == n else B[j]

            if A_left > B_right:     # i is too big
                hi = i - 1
            elif B_left > A_right:   # i is too small
                lo = i + 1
            else:                    # just right
                if (m + n) % 2 == 1:
                    return float(min(A_right, B_right))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2