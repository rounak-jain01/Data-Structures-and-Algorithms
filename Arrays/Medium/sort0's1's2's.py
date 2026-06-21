class SortArray:
    def bruteforce(arr):
        arr.sort()
    
    def better(arr):
        count0, count1, count2 = 0, 0, 0
        for i in arr:
            if i == 0:
                count0 += 1
            elif i == 1:
                count1 += 1
            else:
                count2 += 1

        index = 0
        for i in range(count0):
            arr[index] = 0
            index+=1
        for i in range(count1):
            arr[index] = 1
            index+=1
        for i in range(count2):
            arr[index] = 2
            index+=1
        
        return arr
    
    def optimal(arr):
        low, mid, high = 0,0,len(arr)-1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr


obj = SortArray
arr = [2,0,1,0,2,1]
obj.optimal(arr)
print(arr)