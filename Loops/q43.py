# GCD (HCF) of two numbers find karo using loop (Euclidean 
# algorithm).

def hcf(n,m):

    while m != 0:
        temp = n % m
        n = m
        m = temp

    print(n)


hcf(96,6)