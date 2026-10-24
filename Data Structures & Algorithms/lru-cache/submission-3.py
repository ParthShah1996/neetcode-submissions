from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)      # now the newest
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value          # add or update
        self.cache.move_to_end(key)      # now the newest
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)   # remove the oldest