# Print N - 1 using recursion

def rev_print(i,n):
    if (i < n):
        return
    print(i)
    rev_print(i-1,n)

rev_print(10,1)