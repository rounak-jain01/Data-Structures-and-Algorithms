# Ek sorted list mein binary search implement karo using while loop.

def binary_search(l,key):
    s = 0
    e = len(l) - 1
    mid = (s+e)//2

    while s <= e:
        if l[mid] == key:
            return mid
        
        elif l[mid] < key:
            s = mid + 1
            mid = (s+e)//2
        else:
            e = mid - 1
            mid = (s+e)//2



l = [12,22,32,42,52,62,72]
print(binary_search(l,52))


