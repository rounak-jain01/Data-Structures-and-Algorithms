
class ConsecutiveArraySequence:

    def ls(self, arr,x):
        for i in arr:
            if i == x:
                return True
        return False
    
    def bruteforce(self,arr):
        n = len(arr)
        largest = 1

        for i in range(n):
            x = arr[i]
            cnt = 1
            while self.ls(arr,x+1) == True:
                x = x+1
                cnt += 1
            
            largest = max(largest, cnt)

        return largest
    
    def better(self, arr):
        n = len(arr)
        lastSmaller = float('-inf')
        cnt = 0
        largest = 1
        arr.sort()

        for i in range(n):
            if arr[i] - 1 == lastSmaller:
                cnt += 1
                lastSmaller = arr[i]

            elif arr[i] != lastSmaller:
                cnt = 1
                lastSmaller = arr[i]

            largest = max(largest, cnt)
        return largest
    
    def optimal(self, arr):
        n = len(arr)
        longest = 0
        seen = set(arr)

        for i in seen:
            if i - 1 not in seen:
                cnt = 1
                curr = i
                while curr + 1 in seen:
                    curr += 1
                    cnt += 1

                longest = max(longest, cnt)

        return longest

    
                   


arr = [102,4,100,1,101,3,2,1,1]
obj = ConsecutiveArraySequence()
ans = obj.optimal(arr)
print(ans)