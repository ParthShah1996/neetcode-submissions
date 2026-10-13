class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0


        left = 0
        right = m*n - 1

        while left <= right:
            mid = left + (right-left)//2
            m1 = mid // n
            m2 = mid % n

            if matrix[m1][m2] == target:
                return True
            
            if matrix[m1][m2] < target:
                left = mid + 1
            
            else:
                right = mid - 1

            
        
        return False
        