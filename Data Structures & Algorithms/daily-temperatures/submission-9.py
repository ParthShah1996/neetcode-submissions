class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        length_temp = len(temperatures)
        output = [0] * length_temp
        indices = []
        indices.append(0)

        for i in range(1, length_temp):
            curr_temp = temperatures[i]
            while indices and curr_temp > temperatures[indices[-1]]:
                    j = indices.pop()
                    output[j] = i-j

            indices.append(i)
                
        return output
