class DemoClass:
    def __init__(self,name):
        self.name = name

    def returnName(self):
        return self.name

def __main__():
    obj = DemoClass("Jhon Doe")
    name = obj.returnName()
    print("Hello, "+name)

__main__()
