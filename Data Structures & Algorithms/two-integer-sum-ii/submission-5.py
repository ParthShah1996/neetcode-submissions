class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
    
        i = 0
        j = length - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if target/2 - numbers[i] > numbers[j] - target/2:
                i += 1
            else:
                j -= 1
            
        

        



        