


def moveZeroEnd(arr,n):

    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1,n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j],arr[i]
            j+=1
        

    print (arr)





arr = [1,2,3,0,0,4,0,5,3,0,7,3,0]
moveZeroEnd(arr,len(arr))