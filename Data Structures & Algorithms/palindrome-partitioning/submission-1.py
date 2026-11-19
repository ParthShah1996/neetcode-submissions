class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res: List[List[str]] = []
        path: List[str] = []
        n = len(s)

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int) -> None:
            if start == n:
                res.append(list(path))
                return

            for i in range(start, n):
                if is_palindrome(start, i):
                    path.append(s[start : i + 1])
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)
        return res