class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort(reverse = True)
            print(stones)

            x, y = stones[0], stones[1]
            if x == y:
                print("x==y")
                del stones[1]
                del stones[0]
            else:
                print("x>y")
                del stones[1]
                stones[0] = x-y
            print(
                "FINAL: ", stones
            )
            
        
        if stones:
            print(stones)
            return stones[0]
        else:
            return 0
        