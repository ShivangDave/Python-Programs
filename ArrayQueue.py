class ArrayQueue:
    DEFAULT_CAP = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.DEFAULT_CAP
        self.size = 0
        self.front = 0

    def len(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def first(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        return self.data[self.front]

    def dequeue(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size = -1
        return answer

    def enqueue(self,e):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def resize(self,cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1+walk) % len(old)
        self.front = 0

if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(5)
    print(Q.enqueue(3))
    print(Q)
    print(Q.len())
    print(Q.dequeue())
    print(Q.isEmpty())
