# Additional : Factorial of a number using Recursion

def fact(n):
    # fat = 1
    if n == 0:
        return 1
    n = n *  fact(n-1)
    return n
    
print(fact(5))