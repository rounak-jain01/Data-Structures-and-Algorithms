class MoveZeroToEnd:
    def bruteForce(arr,n):
        temp = []
        for i in range(n):
            if arr[i] != 0:
                temp.append(arr[i])


        for i in range(len(temp)):
            arr[i] = temp[i]

        for i in range(len(temp),n):
            arr[i] = 0

    def optimalApproach(arr,n):
        left = -1
        for i in range(n):
            if arr[i] == 0:
                left = i
                break

        if left == -1:
            return

        for i in range(left + 1,n):
            
            if arr[i] != 0:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
                


obj = MoveZeroToEnd
arr = [1,2,0,4,6,0,0,0,6,3,2,5,6,0]
obj.optimalApproach(arr,len(arr))
print(arr)