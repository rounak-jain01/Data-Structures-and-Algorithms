class MajorityElement:
    def bruteforce(arr):
        n = len(arr)
        for i in range(n):
            count = 0
            for j in range(n):
                if arr[j] == arr[i]:
                    count += 1
            
            if count > n // 2:
                return arr[i]
            
        return "Not Found"

    def better(arr):
        pass

    def optimal(arr):
        pass


obj = MajorityElement
arr = [2,2,1,1,1,2,2,3,3,3,3,3]
print(obj.bruteforce(arr))
