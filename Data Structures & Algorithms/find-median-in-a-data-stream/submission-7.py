import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap for the smaller half (stored as negative numbers)
        self.small = []
        # Min-heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Default push to max-heap
        heapq.heappush(self.small, -num)

        # Step 2: Ensure max of small <= min of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance sizes (small can have at most 1 extra element)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd number of elements, the root of small has the extra element
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If even number of elements, average the two roots
        return (-self.small[0] + self.large[0]) / 2.0