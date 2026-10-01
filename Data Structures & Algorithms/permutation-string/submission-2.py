class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False
        
        left = 0
        right = s1_length
        while right <= s2_length:
            if sorted(s1) == sorted(s2[left:right]):
                return True
            right += 1
            left += 1
        
        return False




        