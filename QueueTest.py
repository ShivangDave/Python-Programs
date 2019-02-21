from Queue import Queue

q = Queue()
q.enqueue("3")
q.enqueue("7")
q.enqueue("10")

for items in range(len(q.items)):
    print(q.items)
    print(q.dequeue())
