class Solution:
   

    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        res = []
        temp = 0
        
        def is_integer(s):
            if not s:
                return False
            return s[1:].isdigit() if s[0] == '-' and len(s) > 1 else s.isdigit()

        operations_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        for c in tokens:
            if c in operations_map:
                temp = operations_map.get(c)(res[-2], res[-1])
                res.pop()
                res.pop()
                res.append(temp)
                
                
            else:
                res.append(int(c))
                
                
        return int(res[0])