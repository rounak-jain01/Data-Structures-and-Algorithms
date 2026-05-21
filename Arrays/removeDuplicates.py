
def remove_duplicate(arr,n):
    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
           i+=1
           arr[i] = arr[j]

    return arr[:i+1] 





arr = [1,1,2,2,3,3]
print(remove_duplicate(arr,len(arr)))
