class Tree:
    class Position:

        def element(self):
            raise NotImplementedError('Must be implemented by Subclass.')

        def eq(self,other):
            raise NotImplementedError('Must be implemented by Subclass.')

        def ne(self,other):
            raise NotImplementedError('Must be implemented by Subclass.')

    def root(self):
        raise NotImplementedError('Must be implemented by Subclass.')

    def parent(self,p):
        raise NotImplementedError('Must be implemented by Subclass.')

    def numChildern(self,p):
        raise NotImplementedError('Must be implemented by Subclass.')

    def children(self,p)
        raise NotImplementedError('Must be implemented by Subclass.')

    def len(self):
        raise raise NotImplementedError('Must be implemented by Subclass.')

    def isRoot(self,p):
        return self.root() == p

    def isLeaf(self,p):
        return self.numChildern(p) == 0

    def isEmpty(self,p):
        return len(self) == 0

    def depth(self,p):
        if self.isRoot(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self,p=None):
        if p is None:
            p = self.root()
        return self.height2(p)

    def height1(self):
        return max(self.depth(p) for p in self.positions() if self.isLeaf(p))

    def height2(self,p):
        if self.isLeaf(p):
            return 0
        else:
            return 1 + max(self.height2(c) for c in self.children(p))
