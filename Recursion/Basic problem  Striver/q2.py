# Print Linearly form 1 - N

def linerarly(i,n):
    if (i > n):
        return 
    print(i,end=" ")
    linerarly(i+1,n)

linerarly(1,50)