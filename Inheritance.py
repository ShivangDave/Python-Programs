class DemoClass:
    def __init__(self,name):
        self.name = name

    def returnName(self):
        return self.name

class SecondClass(DemoClass):
    def __init__(self,name,surname):
        self.surname = surname
        self.name = name
        super().__init__(self.name)

    def returnName(self,x):
        return self.name+x

    def returnFullname(self):
        self.name = super().returnName()
        return self.name + " " + self.surname

def __main__():
    first = input('Enter name: ')
    second = input('Enter surname: ')
    obj = SecondClass(first,second)
    name = obj.returnFullname()
    print("Hello, "+name)

__main__()
