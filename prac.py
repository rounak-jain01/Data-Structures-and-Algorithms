def bubbleSort(arr):
        # code here
    n = len(arr)
    isSwap = False
    
    for i in range(n-1,-1,-1):
        for j in range(1,i+1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                isSwap = True
        if isSwap == False:
            break


def selectionSort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]





arr = [4, 1, 3, 9, 7]
selectionSort(arr)
print(arr)
            