class BinarySearch:
    def __init__(self,list):
        self.list = list

    def searchElement(self,list,number,low,high):
        if low > high:
            return False
        else:
            mid = (low+high) // 2
            if number == list[mid]:
                return True
            elif number < list[mid]:
                return self.searchElement(list,number,low,mid-1)
            else:
                return self.searchElement(list,number,mid+1,high)

def __main__():
    L1 = list(range(100))
    obj = BinarySearch(L1)
    print(obj.searchElement(L1,40,70,120))

__main__()
