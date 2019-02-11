def merge(S1,S2,S):
    while not S1.isEmpty() and not S2.isEmpty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.isEmpty():
        S.enqueue(S1.dequeue())
    while not S2.isEmpty():
        S.enqueue(S2.dequeue())

def mergeSort(S):
    n = len(S)
    if n<2:
        return
    S1 = LinkedQueue()
    S2 = LinkedQueue()
    while len(S1) < n//2:
        S1.enqueue(S.dequeue())
    while not S.isEmpty():
        S2.enqueue(S.dequeue())

mergeSort(S1)
mergeSort(S2)
merge(S1,S2,S)
