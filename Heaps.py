from array import array

class Heap:

    def __init__(self,size=0,capacity=10):
        self.capacity = capacity
        self.size = size
        self.items = array('d')

    def getLeftChildIndex(self,parentIndex):
        return 2*parentIndex+1

    def getrightChildIndex(self,parentIndex):
        return 2*parentIndex+2

    def getParentIndex(self,childIndex):
        return (childIndex-1)//2

    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self,index):
        return self.getrightChildIndex(index) < self.size

    def hasParent(self,index):
        return self.getParentIndex(index) >= 0

    def leftChild(self,index):
        return self.items[self.getLeftChildIndex(index)]

    def rightChild(self,index):
        return self.items[self.getrightChildIndex(index)]

    def parent(self,index):
        return self.items[self.getParentIndex(index)]

    def swap(self,indexOne,indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp

    def ensureExtraCapacity(self):
        if self.size == self.capacity:
            self.capacity *= 2

    def peek(self):
        if self.size == 0:
            raise IllegalStateException()
        return self.items[0]

    def poll(self):
        if self.size == 0:
            raise IllegalStateException()
        item = self.items[0]
        self.items[0] = self.items[self.size-1]
        self.size -= 1
        self.heapifyDown()
        return item

    def add(self,item):
        self.ensureExtraCapacity()
        #self.items[self.size] = item
        self.items.append(item)
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while(self.hasParent(index) and self.parent(index) > self.items[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallChildIndex = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallChildIndex = self.getrightChildIndex(index)
            if(self.items[index] < self.items[smallChildIndex]):
                break
            else:
                self.swap(index,smallChildIndex)
            index = smallChildIndex
