def partition(arr,st,end):
    pIndex = arr[end]
    idx = st-1

    for i in range(st,end):
        if arr[i] <= pIndex:
            idx+=1
            arr[idx],arr[i] = arr[i],arr[idx]
    idx+=1
    arr[idx],arr[end] = arr[end],arr[idx]
    return idx


def quickSort(arr, st, end):
    if st < end:
        pIndex = partition(arr, st, end)
        quickSort(arr,st,pIndex-1)
        quickSort(arr,pIndex+1,end)


arr = [4,5,1,3,6]
quickSort(arr,0,len(arr)-1)
print(arr)