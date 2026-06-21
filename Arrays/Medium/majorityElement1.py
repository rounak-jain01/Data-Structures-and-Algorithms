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
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for key, value in freq.items():
            if value > len(arr) // 2:
                return key

    def optimal(arr):
        candidate = None
        count = 0

        for i in arr:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1

        count = 0
        for num in arr:
            if num == candidate:
                count += 1

        if count > len(arr) // 2:
            return candidate

        return "Not Found"


obj = MajorityElement
arr = [2,2,1,1,1,2,2]
print(obj.optimal(arr))
