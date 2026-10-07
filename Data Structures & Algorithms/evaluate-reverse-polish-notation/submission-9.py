class Solution:
   

    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        res = []
        temp = 0
        def is_integer(s):
            if not s:
                return False
            # If it starts with '-', check if the rest is digits. Otherwise, check the whole thing.
            return s[1:].isdigit() if s[0] == '-' and len(s) > 1 else s.isdigit()
        operations_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        for c in tokens:
            if is_integer(c):
                res.append(int(c))
            else:
                temp = operations_map.get(c)(res[-2], res[-1])
                res.pop()
                res.pop()
                res.append(temp)
                
                
        return int(res[0])