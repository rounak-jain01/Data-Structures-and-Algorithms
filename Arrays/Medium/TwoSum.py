def twosum(arr, tar):
    d = {}
    for i in range(len(arr)):
        f = arr[i]
        s = tar - f

        if s in d:
            return [i,d[s]]
        
        d[f] = i 

arr = [1, -2, 1, 0, 5]
t = 0
print(twosum(arr,t))