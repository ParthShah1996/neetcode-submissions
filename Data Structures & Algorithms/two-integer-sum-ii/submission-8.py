class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
    
        i = 0
        j = length - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i+1, j+1]
            if current_sum < target:
                i += 1
            else:
                j -= 1
            
        

        



        