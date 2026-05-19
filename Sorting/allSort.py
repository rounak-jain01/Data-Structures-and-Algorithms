def selectionSort(arr,n):

    for i in range(0,n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]

def bubbleSort(arr,n):
    for i in range(n-1,-1,-1):
        isSwap = False
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                isSwap = True

        if isSwap == False:
            break
                

def insertionSort(arr,n):
    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        while prev >= 0 and arr[prev] >= curr:
            arr[prev+1] = arr[prev]
            prev-=1
        arr[prev+1] = curr
    

def mergesort(arr, low, high):
    if low == high:
        return
    mid = (low + high)//2

    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left = low
    right = mid +1
    temp = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while(left <= mid):
        temp.append(arr[left])
        left += 1

    while right <= mid:
        temp.append(arr[right])
        right += 1

    for i in range(len(temp)):
        arr[low+i] = temp[i]



def quickSort(arr,st, end):
    if st < end:
        pindex = partition(arr,st,end)
        quickSort(arr,st,pindex-1)
        quickSort(arr,pindex+1,end)


def partition(arr,st,end):
    pivot = arr[end]
    idx = st-1

    for i in range(st,end):
        if arr[i] <= pivot:
            idx+=1
            arr[i], arr[idx] = arr[idx],arr[i]
    idx+=1
    arr[idx],arr[end] = arr[end],arr[idx]

    return idx   
    
    

arr = [4,1,6,7,8,2,9,3]
# insertionSort(arr,len(arr))
# mergesort(arr, 0, len(arr)-1)
quickSort(arr,0,len(arr)-1)
print(arr)