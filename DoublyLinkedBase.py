class DoublyLinkedBase:
    class Node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def __init__(self):
        self.header = self.Node(None,None,None)
        self.trailer = self.Node(None,None,None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def len(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertBetween(self,e,predecessor,successor):
        newest = self.Node(e,predecessor,successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def deleteNode(self,node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element

if __name__ == '__main__':
    print('Program Compiled')
