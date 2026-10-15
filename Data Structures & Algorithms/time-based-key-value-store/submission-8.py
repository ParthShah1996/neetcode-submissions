class TimeMap:

    def __init__(self):
        self.store = {}   # key -> list of (timestamp, value), sorted by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        items = self.store.get(key, [])
        result = ""
        start, end = 0, len(items) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if items[mid][0] <= timestamp:     # Yes
                result = items[mid][1]         # remember it, it may be the last Yes
                start = mid + 1
            else:                              # No
                end = mid - 1

        return result