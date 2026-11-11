from collections import OrderedDict
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

            
        
