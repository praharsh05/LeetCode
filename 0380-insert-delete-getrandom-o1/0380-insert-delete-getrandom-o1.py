class RandomizedSet:

    def __init__(self):
        self.RadomizedSet = []
        self.hashSet = {}
    
    def search(self, val: int):
        return val in self.hashSet

    def insert(self, val: int) -> bool:
        if self.search(val): return False
        
        self.RadomizedSet.append(val)
        self.hashSet[val] = len(self.RadomizedSet)-1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val): return False
        
        index = self.hashSet[val]
        self.RadomizedSet[index] = self.RadomizedSet[-1]
        self.hashSet[self.RadomizedSet[-1]] = index
        self.RadomizedSet.pop()
        del self.hashSet[val]
        return True

    def getRandom(self) -> int:
        import random
        index = random.randint(0, len(self.RadomizedSet)-1)
        return self.RadomizedSet[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()