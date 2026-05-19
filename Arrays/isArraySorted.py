class isArraySorted:
    def bruteForce(arr,n):
        small = arr[0]
        isSorted = True
        for i in range(n):
            if arr[i] < small:
                isSorted = False
            small = arr[i]
            
        return isSorted
    
obj = isArraySorted
arr = [1,2,3,4,5,9,0 ]
print(obj.bruteForce(arr,len(arr)))