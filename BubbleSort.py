class BubbleSort:

    def __init__(self,list):
        self.list = list
        self.totalPasses = 0

    def sort(self):
        isSorted = False
        lastUnsorted = len(self.list) - 1

        while(isSorted is False):
            isSorted = True
            for i in range(lastUnsorted):
                if self.list[i] > self.list[i+1]:
                    self.swap(i,i+1)
                    isSorted = False
                    self.totalPasses += 1
            lastUnsorted -= 1
        return isSorted

    def swap(self,i,j):
        self.list[i], self.list[j] = self.list[j], self.list[i]
