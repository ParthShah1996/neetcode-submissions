class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        
        q = deque()

        for c in s:
            print(q)
            if c in bracket_map:
                q.append(c)
            elif q and c == bracket_map[q[-1]]:
                q.pop()
            else:
                return False
        return not bool(q)


        
        