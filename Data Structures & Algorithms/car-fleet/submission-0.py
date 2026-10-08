class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [0] * n


        # Pairing and Sorting the Position and Speed of each car.
        pairs = list(zip(position, speed))
        pairs.sort(reverse = True)

        # Calculating time for each car
        for i, (pos, spd) in enumerate(pairs):
            time[i] = (target - pos)/spd
        
        fleet = 1
        max_time = time[0]
        for i in range(1, n):
            if max_time < time[i]:
                max_time = time[i]
                fleet += 1
            else:
                continue

        
        return fleet

        

        