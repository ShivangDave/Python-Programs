class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,value):
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self,value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print(self.value)
        if self.right is not None:
            self.right.printInOrder()

    def printPreOrder(self):
        print(self.value)
        if self.left is not None:
            self.left.printPreOrder()
        if self.right is not None:
            self.right.printPreOrder()

    def printPostOrder(self):
        if self.left is not None:
            self.left.printPostOrder()
        if self.right is not None:
            self.right.printPostOrder()
        print(self.value)
