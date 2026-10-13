class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_pile = max(piles)
        start = 1
        end = max_pile
        
        while start <= end:
            mid = (start + end)//2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1)//mid
                        
            if hours <= h:
                end = mid - 1
            else:
                start = mid + 1

        return start
                
            





        

        