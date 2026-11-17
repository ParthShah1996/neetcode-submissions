class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res =  0
        maxf = 0

        for right in range(len(s)):
            curr_char = s[right]
            count[curr_char] = 1 + count.get(curr_char, 0)
            maxf = max(maxf, count[curr_char])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
        
        

        