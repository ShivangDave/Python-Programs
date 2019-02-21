# Reference: https://www.youtube.com/watch?v=CB_NCoxzQnk

class QuickSort:
    def __init__(self,list):
        self.list = list

    def sort(self):
        return self.quickSort(self.list,0,len(self.list)-1)

    def quickSort(self,list,low,high):
        if low<high:
            p = self.partition(list,low,high)
            self.quickSort(list,low,p-1)
            self.quickSort(list,p+1,high)
        return list

    def getPivot(self,list,low,high):
        mid = (high+low)//2
        pivot = high
        if list[low] < list[mid]:
            if list[mid] < list[high]:
                pivot = mid
        elif list[low]<list[high]:
            pivot = low
        return pivot

    def partition(self,list,low,high):
        pivotIndex = self.getPivot(list,low,high)
        pivotValue = list[pivotIndex]
        list[pivotIndex],list[low] = list[low],list[pivotIndex]
        border = low

        for i in range(low,high+1):
            if list[i]<pivotValue:
                border += 1
                list[i],list[border] = list[border],list[i]
        list[low],list[border] = list[border],list[low]
        return border

    def swap(self,list,i,j):
        list[i],list[j] = list[j],list[i]
        return list
