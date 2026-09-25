class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)
        kList =[]
        for i in range(0,k):
            kList.append(sorted_count[i][0])
        return kList
