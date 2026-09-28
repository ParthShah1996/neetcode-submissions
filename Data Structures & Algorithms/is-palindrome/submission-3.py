class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 # Left Pointer
        j = len(s) - 1 # right pointer
    
        while i < j:
            if not self.alphaNum(s[i]):
                i += 1 
            
            elif not self.alphaNum(s[j]):
                j -= 1
            
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            
        return True

    def alphaNum(self, c):
        return ( ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
    