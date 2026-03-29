class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # init capacity and cache for O(1) lookups
        self.cap = capacity
        self.cache = {}

        # Create doubly linked list of two dummy nodes
        self.leftMost, self.rightMost = Node(0,0), Node(0,0)
        self.leftMost.next, self.rightMost.prev = self.rightMost, self.leftMost

    def insert(self, node):
        # Insert node at the end of the list (just before rightMost)
        currPrev, currNext = self.rightMost.prev, self.rightMost
        currPrev.next = currNext.prev = node
        node.next, node.prev = currNext, currPrev

    def remove(self, node):
        # Connect removed nodes prev to next and vice versa
        currPrev, currNext = node.prev, node.next
        currPrev.next, currNext.prev = currNext, currPrev

    def get(self, key: int) -> int:
        # Remove key from cache and insert at right end (most recently used)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # Add new node to the right
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If at capacity, remove LRU
        if len(self.cache) > self.cap:
            lru = self.leftMost.next
            self.remove(lru)
            del self.cache[lru.key]