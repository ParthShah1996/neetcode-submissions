class TimeMap:

    def __init__(self):
        self.key_value = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.key_value:
            self.key_value = {key: [(timestamp, value)]}
        elif key not in self.key_value:
            self.key_value[key] = [(timestamp, value)]
        else:
            self.key_value[key].append((timestamp, value))
       

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.key_value:
            return ""

        start = 0
        end = len(self.key_value[key]) - 1
        if timestamp < self.key_value[key][start][0]:
            return ""

        while start <= end:
            mid = start + (end - start)//2
        
            if timestamp == self.key_value[key][mid][0]:
                return self.key_value[key][mid][1]
            
            if timestamp < self.key_value[key][mid][0]:
                end = mid - 1
            else:
                start = mid + 1

        return self.key_value[key][end][1]
