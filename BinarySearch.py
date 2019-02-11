def binarySearch(list,number,low,high):
    if low > high:
        return False
    else:
        mid = (low+high) // 2
        if list[mid] == number:
            return True
        elif number < list[mid]:
            return binarySearch(list,number,low,mid-1)
        else:
            return binarySearch(list,number,mid+1,high)
    return False

L1 = list(range(100))
print(binarySearch(L1,40,0,50))
