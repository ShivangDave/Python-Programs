class ArrayStack:

    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def length(self):
        return len(self.data)

    def push(self,e):
        self.data.append(e)

    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty.')
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty.')
        return self.data[-1]

if __name__ == '__main__':
    S = ArrayStack()
    S.push(3)
    S.push(5)
    print(S.pop())
    print(S.isEmpty())
    print(S.top())
    print(S.length())
