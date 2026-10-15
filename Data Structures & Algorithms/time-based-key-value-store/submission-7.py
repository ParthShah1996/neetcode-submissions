class TimeMap:

    def __init__(self):
        self.pairs = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.pairs:
            self.pairs = {key: [(timestamp, value)]}
        elif key not in self.pairs:
            self.pairs[key] = [(timestamp, value)]
        else:
            self.pairs[key].append((timestamp, value))
       

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.pairs:
            return ""

        start = 0
        end = len(self.pairs[key]) - 1
        if timestamp < self.pairs[key][start][0]:
            return ""

        while start <= end:
            mid = start + (end - start)//2
        
            if timestamp == self.pairs[key][mid][0]:
                return self.pairs[key][mid][1]
            
            if timestamp < self.pairs[key][mid][0]:
                end = mid - 1
            else:
                start = mid + 1

        return self.pairs[key][end][1]
