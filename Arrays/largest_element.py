def largest_element(arr):
    maxi = arr[0]
    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi

arr = [1,6,8,9,4,6,3]
print(largest_element(arr))