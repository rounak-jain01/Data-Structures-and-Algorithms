# Reverse Array using Recursion

def func1(i,j):
    if i >= j:
        return l
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
    
    return func1(i+1,j-1)


def func2(i, n):
    if i >= n // 2:
        return l

    l[i], l[n-i-1] = l[n-i-1], l[i]

    return func2(i + 1, n)


l = [1,2,3,4,5] # [5, , , ,1]

print(func2(0, len(l)))