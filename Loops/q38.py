# Ek number prime hai ya nahi check karo using loop.
import math
def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

print(check_prime(19))