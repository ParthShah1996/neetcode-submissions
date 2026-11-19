class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def backtrack(path, start):
            if digits and len(path) == len(digits):
                res.append("".join(path))
                return
            for d in range(start , len(digits)):
                for c in digit_map[digits[d]]:
                    path.append(c)
                    backtrack(path, d+1)
                    path.pop()
             
        backtrack([], 0)

        return res