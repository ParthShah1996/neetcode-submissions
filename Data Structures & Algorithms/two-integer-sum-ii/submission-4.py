class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        # if target > numbers[-1]:
        #     half = length - 1

        # else: 
        #     half = length//2

        #     while target <= numbers[half] and half != 1:
        #             half = half//2
        
        # if half == 1:
        #     return [1, 2]
        
        i = 0
        j = length - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if abs(target/2 - numbers[i]) > abs(target/2 - numbers[j]):
                i += 1
            else:
                j -= 1
            
        

        



        