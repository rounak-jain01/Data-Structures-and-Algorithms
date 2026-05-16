def insertionSort(arr,n):
    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        while (prev >= 0 and arr[prev] > curr):
            arr[prev + 1] = arr[prev]
            prev-=1
        arr[prev + 1] = curr
    
    return arr

arr = [4,3,5,1,2]
print(insertionSort(arr, len(arr)))