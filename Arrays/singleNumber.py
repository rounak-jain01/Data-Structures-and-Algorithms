class SingleNumber:
    def bruteforce(arr):
        n = len(arr)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    cnt += 1
                
            if cnt == 1:
                return arr[i]
    
    def betterApproach(arr):
        n = len(arr)
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for key, value in freq.items():
            if value == 1:
                return key
            
    def optimal(arr):
        single = 0
        for i in arr:
            single = single ^ i
        
        print(single)

            
        



obj = SingleNumber
arr = [1,1,2,2,3,4,4,5,5]
print(obj.optimal(arr))