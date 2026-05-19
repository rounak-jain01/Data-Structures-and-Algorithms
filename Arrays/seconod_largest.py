
class SecondLargest:
    def bruteforce(arr, n):
        arr.sort()
        largest = arr[n-1]
        for i in range(n-2,-1,-1):
            if arr[i] != largest:
                sec = arr[i]
                break

        return sec
    
    def optimalApproach(arr,n):
        largest = arr[0]
        secLatgest = -1 

        for i in range(n):
            if arr[i] > largest:
                secLatgest = largest
                largest = arr[i]

            elif arr[i] < largest and arr[i] > secLatgest:
                secLatgest = arr[i]

        return secLatgest

    




obj = SecondLargest
arr = [10,10,1,2,5,2,7,9,9,5,4]
print(obj.optimalApproach(arr ,len(arr)))