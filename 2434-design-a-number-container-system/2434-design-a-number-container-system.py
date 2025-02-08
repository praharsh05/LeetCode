class NumberContainers:

    def __init__(self):
        # Dictonary to store index and number
        self.index_val = {}
        # Priority Queue to keep track of the smallest index for each number
        self.res = {}

    def change(self, index: int, number: int) -> None:
        # If index and number already present in the hashmap
        if index in self.index_val:
            if self.index_val[index] == number:
                return
        # When index not in hashmap, add the number at the index in the hashmap
        self.index_val[index] = number
        # if number not in priority queue then initialize an empty list to priority queue
        if number not in self.res:
            self.res[number] = []
        # Push the index to the list of the indexes in the priority queue
        heapq.heappush(self.res[number], index)

    def find(self, number: int) -> int:
        # If the number is not in priority queue then return -1
        if number not in self.res: return -1

        # Get the min index
        while self.res[number] and self.index_val[self.res[number][0]] != number:
            heapq.heappop(self.res[number])
        
        return self.res[number][0] if self.res[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)