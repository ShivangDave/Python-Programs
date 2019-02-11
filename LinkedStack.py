class LinkedStack:

    class Node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def len(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self,e):
        self.head = self.Node(e,self.head)
        self.size += 1

    def top(self):
        if self.isEmpty():
            raise Empty('List is empty.')
        return self.head.element

    def pop(self):
        if self.isEmpty():
            raise Empty('List is empty.')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer

if __name__ == '__main__':
    L = LinkedStack()
    L.push(3)
    L.push(5)
    L.push(9)
    print(L.top())
    print(L)
    print(L.pop())
    print(L.top())
