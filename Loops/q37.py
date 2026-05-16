# N tak ke saare Fibonacci numbers print karo.

def fibonacci_series(n):
    a = 0
    b = 1

    for i in range(1,n+1):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp

fibonacci_series(10)