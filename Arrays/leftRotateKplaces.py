
class LeftRotate:

    def reverse(self,arr,st,end):
        while (st < end):
            arr[st], arr[end] = arr[end], arr[st]
            st += 1
            end -=1

        return arr
    
    def bruteForce(self,arr,n,k):
        temp = []
        for i in range(k):
            temp.append(arr[i])

        for i in range(k,n):
            arr[i-k] = arr[i]


        for i in range(n-k,n):
            arr[i] = temp[i - (n - k)]

    def optimalApproach(self,arr,n,k):
        self.reverse(arr,0,k)
        self.reverse(arr,k,n)
        self.reverse(arr,0,n)

        print(arr)


obj = LeftRotate()
arr = [5,1,4,2,7,9,0,7,5]
obj.bruteForce(arr,len(arr),4)
print(arr)