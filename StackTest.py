from Stack import Stack

s = Stack()
s.push("3")
s.push("7")
s.push("10")

for items in range(len(s.items)):
    print(s.items)
    print(s.pop())
