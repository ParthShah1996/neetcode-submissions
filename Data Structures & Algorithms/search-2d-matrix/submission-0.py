class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_array = []
        for arr in matrix:
            for item in arr:
                flattened_array.append(item)
        
        left = 0
        right = len(flattened_array) - 1

        while left <= right:
            mid = left + (right-left)//2

            if flattened_array[mid] == target:
                return True
            
            if flattened_array[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1

            
        
        return False
        