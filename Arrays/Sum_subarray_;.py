class SumofSubArrayk:
    def bruteforce(arr,k):
        n = len(arr)
        count = 0
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum += arr[j]
                if sum == k:
                    count += 1
        
        return count
    
    def optimal(arr,k):
        n = len(arr)
        prefixSum = [0]*n
        count = 0
        prefixSum[0] = arr[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] + arr[i]

        d = {}
        for j in range(n):
            if prefixSum[j] == k:
                count += 1

            val = prefixSum[j] - k

            if val in d:
                count += d[val]

            if prefixSum[j] in d:
                d[prefixSum[j]] += 1
            else:
                d[prefixSum[j]] = 1

        return count



obj = SumofSubArrayk
arr = [9,2,3,4,9,8]
print(obj.optimal(arr,9))