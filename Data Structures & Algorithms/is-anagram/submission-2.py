class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringtMap = {}
        stringsMap = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            stringtMap[t[i]] = stringtMap.get(t[i], 0) + 1 
            stringsMap[s[i]] = stringsMap.get(s[i], 0) + 1 

        if stringtMap == stringsMap:
            return True
        return False



        