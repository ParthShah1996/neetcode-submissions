class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        nums1_left = 0
        nums2_left = 0

        sorted_list = []

        while nums1_left < m or nums2_left < n:
            if nums1_left < m and (nums2_left >= n or nums1[nums1_left] < nums2[nums2_left]):
                sorted_list.append(nums1[nums1_left])
                nums1_left += 1
            else:
                sorted_list.append(nums2[nums2_left])
                nums2_left += 1

        total = m + n
        if total % 2 == 0:
            return (sorted_list[total // 2] + sorted_list[total // 2 - 1]) / 2
        else:
            return float(sorted_list[total // 2])