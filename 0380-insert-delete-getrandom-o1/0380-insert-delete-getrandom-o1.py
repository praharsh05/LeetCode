class RandomizedSet:

    def __init__(self):
        self.RadomizedSet = []
        

    def insert(self, val: int) -> bool:
        if val in self.RadomizedSet: return False
        self.RadomizedSet.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.RadomizedSet:
            self.RadomizedSet.remove(val)
            return True
        else: return False

    def getRandom(self) -> int:
        import random
        index = random.randint(0, len(self.RadomizedSet)-1)
        return self.RadomizedSet[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()