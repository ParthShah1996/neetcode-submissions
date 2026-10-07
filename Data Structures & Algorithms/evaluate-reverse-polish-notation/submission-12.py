class Solution:
   

    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        res = []
        temp = 0

        operations_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }

        for c in tokens:
            if c in operations_map:
                b = res.pop()
                a = res.pop()
                temp = operations_map[c](a, b)
                res.append(temp)
                
                
            else:
                res.append(int(c))
                
        return int(res[0])