# Class Node defining a doubly linked list containing key and val
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # Create a dict to store the key node pair
        self.cap = capacity
        self.cache = {}

        self.oldest = Node(0,0)
        self.latest = Node(0,0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    # Method to remove a node from the linked list
    def remove(self, node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    # Method to add a node into the latest linked list
    def insert(self, node) -> None:
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If length of cache is becomes more than the capacity then drop the oldest node
        if len(self.cache) > self.cap:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)