def reverse(arr, st, end):
    while st < end:
        arr[st], arr[end] = arr[end], arr[st]
        st += 1
        end -= 1

def rightRotate(arr, n, t):
    t %= n
    reverse(arr, n-t,n-1)
    reverse(arr,0,n-t-1)
    reverse(arr, 0, n-1)

arr = [1,5,7,9,3,0,7]
target = 3
rightRotate(arr, len(arr), target)
print(arr)