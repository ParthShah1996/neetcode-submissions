class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                  # key -> node
        self.left = Node(0, 0)           # L: dummy head (LRU side)
        self.right = Node(0, 0)          # R: dummy tail (MRU side)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_end(self, node):      # put it just before R
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert_at_end(self.cache[key])

        if len(self.cache) > self.cap:           # check AFTER adding
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]              # we need lru.key here