class ScoreEntry:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def getname(self):
        return self.name

    def getscore(self):
        return self.score

    def composeString(self):
        return '({0},{1})'.format(self.name,self.score)

def __main__():
    L1 = []
    obj = ScoreEntry('Bob',100)
    L1.append(obj.composeString())
    obj = ScoreEntry('Jhon',50)
    L1.append(obj.composeString())
    print(L1)

__main__()
