class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 # Left Pointer
        j = len(s) - 1 # right pointer
    
        while i < j:
            ci = s[i]
            cj = s[j]
            if not self.alphaNum(ci):
                i += 1 
                continue
            
            elif not self.alphaNum(cj):
                j -= 1
                continue
            
            else:
                if ci.lower() != cj.lower():
                    return False
                i += 1
                j -= 1
            
        return True

    def alphaNum(self, c):
        return ( ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
    