def intersectionArray(a,b):
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    inter = []

    while i < m and j < n:
        if a[i] < b[j]:
            i+=1
        elif a[i] > b[j]:
            j+=1
        else:
            inter.append(a[i])
            i += 1
            j += 1

    print(inter)

a = [1,2,3,3,4,5]
b = [1,3,3,5,6]
intersectionArray(a,b)


