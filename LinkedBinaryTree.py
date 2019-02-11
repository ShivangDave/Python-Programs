class LinkedBinaryTree:
    class Node:
        slots = 'element','parent','left','right'

        def __init__(self,element,parent=None,left=None,right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):

        def __init__(self,container,node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def eq(self,other):
            return type(other) is type(self) and other.node is self.node

    def validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container.')
        if p.node.parent is p.node:
            raise ValueError('p is no longer valid')
        return p.node

    def makePosition(self,node):
        return self.Position(self,node) if node is not None else None


    def __init__(self):
        self.root = None
        self.size = 0

    def len(self):
        return self.size

    def root(self):
        return self.makePosition(self.root)

    def parent(self):
        node = self.validate(p)
        return self.makePosition(node.parent)

    def left(self,p):
        node = self.validate(p)
        return self.makePosition(node.left)

    def right(self,p):
        node = self.validate(p)
        return self.makePosition(node.right)

    def numChildren(self,p):
        node = self.validate(p)
        count = 0

        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def delete(self,p):
        node = self.validate(p)
        if self.numChildren(p) == 2: raise ValueError('p has two children')
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self.root:
            self.root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node
        return node.element

    def attach(self,p,t1,t2):
        ndoe = self.validate(p)
        if not self.isLeaf(p): raise ValueError('Position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self.size += len(t1) + len(t2)
        if not t1.isEmpty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0
        if not t2.isEmpty():
            t2.root.parent = node
            node.right = t2.root
            t2.root = None
            t2.size = 0
