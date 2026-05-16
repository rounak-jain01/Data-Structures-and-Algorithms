


def mergeSort(arr, low, high):
    if low == high:
        return
    
    mid = (low + high) // 2

    # Left half
    mergeSort(arr, low, mid)
    # rightHalf
    mergeSort(arr,mid+1,high)
    # Merge Func
    return merge(arr,low,mid,high)

    

def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid+1

    while (i <= mid and j <= high):
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    
    while i <= mid:
        temp.append(arr[i])
        i+=1
    
    while j <= high:
        temp.append(arr[j])
        j+=1
    
    for k in range(0,len(temp)):
        arr[low+k] = temp[k]

    # return arr


arr = [3,5,1,2]
mergeSort(arr,0,len(arr)-1)
print(arr)