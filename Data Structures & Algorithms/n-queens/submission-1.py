class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)
        
        def backtrack(row):
            if len(path) == n:
                # Wrap the joined string in brackets [] to create a List[str]
                res.append(path.copy())
                return

           
            for col in range(n):
                if (col in cols) or (row+col in pos_diag) or (row-col in neg_diag):
                    continue
                else:
                    cols.add(col)
                    pos_diag.add(row+col)
                    neg_diag.add(row-col)
                    s = "." * col + "Q" + "." * (n-col-1)
                    path.append(s)
                    backtrack(row + 1)
                    cols.remove(col)
                    pos_diag.remove(row+col)
                    neg_diag.remove(row-col)
                    path.pop()

        backtrack(0)
        return res
