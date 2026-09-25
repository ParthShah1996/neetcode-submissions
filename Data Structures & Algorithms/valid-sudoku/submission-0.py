class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Defining collection of hashmaps for each row, column and 3x3 square grid
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9): # Looping through the rows
            for c in range(9): # Looping through the columns in each row
                if board[r][c] == ".": # Check if cell is empty and continue 
                    continue    
                if ((board[r][c] in rows[r]) or # Check if number is in row
                (board[r][c] in columns[c]) or # Check if number is in column
                (board[r][c] in squares[(r//3, c//3)])): # Check if number is in 3x3 square grid                
                    return False
                rows[r].add(board[r][c]) 
                columns[c].add(board[r][c]) 
                squares[(r//3, c//3)].add(board[r][c]) 
                
        return True
