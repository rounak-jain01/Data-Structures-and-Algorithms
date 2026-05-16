# 1 se N tak saare prime numbers print karo (Sieve concept samjho)

import math
def check_prime(n):
    if n == 0 or n == 1:
        return n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return
    
    return n


n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(check_prime(i))

