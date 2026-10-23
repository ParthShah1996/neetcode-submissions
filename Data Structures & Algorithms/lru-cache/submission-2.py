from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        # Create a OrderedDict to store key-value pairs
        self.LRU_map = OrderedDict()
        self.capacity = capacity
        self.items = 0 # To count number of items added
        

    def get(self, key: int) -> int:
        # Check if key exist LRU_map and return value otherwise return -1.
        if key in self.LRU_map:
            self.LRU_map.move_to_end(key) # Move Recently accessed key to the end.
            return self.LRU_map[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.LRU_map:
            self.LRU_map[key] = value
            self.LRU_map.move_to_end(key) # Move Recently added key to the end.

        elif self.items < self.capacity:
            self.items += 1
            self.LRU_map[key] = value
            self.LRU_map.move_to_end(key) # Move Recently added key to the end.

        else:
            self.LRU_map.popitem(last=False) # Remove First item in OrderedDict
            self.LRU_map[key] = value
            self.LRU_map.move_to_end(key) # Move Recently added key to the end.
        
