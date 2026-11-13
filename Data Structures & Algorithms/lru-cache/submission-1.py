from collections import OrderedDict
class Node:
    def __init(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memo = {}

        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next
        

    def get(self, key: int) -> int:

        if sel.key in self.memo:
            self.remove(self.memo[key])
            self.insert(self.memo[key])
            return self.memo[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if self.key in self.memo:
            self.remove(self.memo[key])
        self.memo[key] = self.val
        self.insert(self.memo[key])
        
        if len(self.memo) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.memo[lru.key]



class LRUCache:
    def __init__(self, capacity: int):
        

        self.capacity = capacity
        self.memo = OrderedDict()

        

    def get(self, key: int) -> int:

        if key in self.memo:
            self.memo.move_to_end(key)
            return self.memo[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.memo:
            self.memo.move_to_end(key)
        self.memo[key] = value
        
        if len(self.memo) > self.capacity:
            self.memo.popitem(last=False)

        
