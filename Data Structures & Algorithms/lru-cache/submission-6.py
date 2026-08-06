class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = deque()
        self.length = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None: 
        if key in self.cache:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        elif self.length < self.capacity:
            self.cache[key] = value
            self.queue.append(key)
            self.length += 1
        else:
            key_popped = self.queue.popleft()
            self.cache.pop(key_popped)
            self.cache[key] = value
            self.queue.append(key)
            
        
