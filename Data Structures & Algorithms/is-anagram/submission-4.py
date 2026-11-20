class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_t = {}
        char_s = {}

        if len(s) != len(t):
            return False

        for i in range(len(t)):
            char_t[t[i]] = 1 + char_t.get(t[i],0)
            char_s[s[i]] = 1 + char_s.get(s[i],0)

        if char_t == char_s:
            return True 
        return False