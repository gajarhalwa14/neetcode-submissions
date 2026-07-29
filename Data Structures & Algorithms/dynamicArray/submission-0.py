class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        k = self.getSize()
        if (k == self.capacity):
            self.resize()
        self.array[k] = n


    def popback(self) -> int:
        k = self.getSize() - 1
        retVal = self.array[k]
        self.array[k] = None
        return retVal
 

    def resize(self) -> None:
        oldArray = self.array;
        oldSize = self.getSize()
        self.capacity *= 2
        self.array = [None] * (self.capacity)
        i = 0
        for index in range(oldSize):
            self.array[index] = oldArray[index]



    def getSize(self) -> int:
        i = 0
        while (self.array[i] != None):
            i += 1
            if (i == self.capacity):
                return self.capacity
        return i
    
    def getCapacity(self) -> int:
        return self.capacity