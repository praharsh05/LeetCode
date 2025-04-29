class RandomizedSet:

    def __init__(self):
        self.randomizedSet = []
        self.hashset = {}
    
    def search(self, val: int) -> bool:
        return val in self.hashset

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        
        self.randomizedSet.append(val)
        self.hashset[val] = len(self.randomizedSet) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        
        index = self.hashset[val]
        self.randomizedSet[index] = self.randomizedSet[-1]
        self.hashset[self.randomizedSet[-1]] = index
        self.randomizedSet.pop()
        del self.hashset[val]
        return True

    def getRandom(self) -> int:
        import random
        index = random.randint(0, len(self.randomizedSet) - 1)
        return self.randomizedSet[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()