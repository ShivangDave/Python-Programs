class Queue:
    def __init__(self,items=[]):
        self.items = items

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]

    def enqueue(self,value):
        self.items.insert(0,value)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
