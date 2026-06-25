class LeadersinArray:
    def brute(arr):
        n = len(arr)
        ans = []

        for i in range(n):
            isLeader = True
            for j in range(i+1,n):
                if arr[j] > arr[i]:
                    isLeader = False
                    break
            
            if isLeader:
                ans.append(arr[i])

        return ans
    

    def optimal(arr):
        n = len(arr)
        ans = []

        rightmax = arr[n-1]
        ans.append(rightmax)

        for i in range(n-2,-1,-1):
            if arr[i] > rightmax:
                ans.append(arr[i])
                rightmax = arr[i]

        
        ans.reverse()
        return ans

        


obj = LeadersinArray
arr = [10,22,12,3,0,6]
ans = obj.optimal(arr)
print(ans)