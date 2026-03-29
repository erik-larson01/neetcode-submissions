class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # init capacity and cache for O(1) lookups
        self.cap = capacity
        self.cache = {}

        # Create doubly linked list of two nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        currPrev, currNext = self.right.prev, self.right
        currPrev.next = currNext.prev = node
        node.next, node.prev = currNext, currPrev

    def remove(self, node):
        currPrev, currNext = node.prev, node.next
        currPrev.next, currNext.prev = currNext, currPrev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]