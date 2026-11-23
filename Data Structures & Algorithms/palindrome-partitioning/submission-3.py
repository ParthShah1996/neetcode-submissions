class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(path, start):
            if start == len(s):
                res.append(list(path))
                return
                
            for i in range(start, len(s)):
                left = start
                right = i
                is_palindrome = True
                while left < right:
                    if s[left] != s[right]:
                        is_palindrome = False
                        break
                    else:
                        left += 1
                        right -= 1
                if is_palindrome:
                    path.append(s[start:i+1])
                    backtrack(path, i + 1)
                    path.pop()
            
        backtrack([], 0)
        return res

        