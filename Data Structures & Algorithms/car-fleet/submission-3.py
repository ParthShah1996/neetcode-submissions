class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Pairing and Sorting the Position and Speed of each car.
        pairs = sorted(zip(position, speed), reverse=True)

        fleets = 0
        max_time = 0

        # Calculating time for each car
        for pos, spd in pairs:
            time = (target - pos)/spd
            if time > max_time:
                max_time = time
                fleets += 1
        
        return fleets