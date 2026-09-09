class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for s in strs:
            encodeStr += str(len(s)) +  "#" + s
        return encodeStr

    def decode(self, s: str) -> List[str]:
        decodeStr, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            decodeStr.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return decodeStr
