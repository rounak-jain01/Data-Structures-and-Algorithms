def missingNumber(arr,n):
    total = n*((n+1)//2)
    missum = 0

    for i in arr:
        missum += i

    return total - missum

def Optimal2Approach(arr):
    xor1 = 0
    xor2 = 0
    n = len(arr)

    for i in range(n):
        xor2 = xor2 ^ arr[i]
        xor1 = xor1 ^ i

    xor1 = xor1 ^ (n)
    return xor1 ^ xor2

arr = [3,0,1]
print(Optimal2Approach(arr))
