

def bubbleSort(arr,n):
    for i in range(n-1,-1,-1):
        isSwap = False
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                isSwap = True

        if isSwap == False:
            break
    return arr

arr = [13,40,24,52,6,9]
print(bubbleSort(arr,len(arr)))