class MergeSort:

    def __init__(self,list):
        self.list = list

    def sort(self):
        return self.mergeSort(self.list)

    def mergeSort(self,list):
        if len(list)>1:
            middle = len(list)//2
            left = list[:middle]
            right = list[middle:]
            self.mergeSort(left)
            self.mergeSort(right)
            self.merge(list,left,right)

            return list

    def merge(self,list,left,right):
        i,j,k = 0,0,0

        while(i<len(left) and j<len(right)):
            if(left[i] < right[j]):
                list[k] = left[i]
                i+=1
            else:
                list[k] = right[j]
                j+=1
            k+=1

        while(i<len(left)):
            list[k] = left[i]
            k+=1
            i+=1

        while(j<len(right)):
            list[k] = right[j]
            k+=1
            j+=1

        return list
