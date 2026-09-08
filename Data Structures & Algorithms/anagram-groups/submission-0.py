class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for two anagrams I can count the number of characters of each string using a hashmap
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26 # a ... z

            for c in str:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(str)
        
        return list(res.values())
            