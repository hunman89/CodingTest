class RandomizedSet:
    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.indices: return False
        
        self.arr.append(val)
        self.indices[val] = len(self.arr)-1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.indices: return False

        # O(1)
        idxRm = self.indices[val]        
        self.arr[idxRm] = self.arr[-1]        
        self.indices[self.arr[idxRm]] = idxRm        
        self.indices.pop(val)
        self.arr.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)