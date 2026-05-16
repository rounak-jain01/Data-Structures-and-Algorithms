# print 1 - N using backtracking recursion

def linearly(i,n):
    if i < n:
        return
    linearly(i-1,n)
    print(i)

linearly(10,1)