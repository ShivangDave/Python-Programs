def insertion_sort(A):
    for k in range(1,len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

L = [90,100,101,102,103,104,104,844,10,20,30,40,50,60,70,80]
print(insertion_sort(L))
