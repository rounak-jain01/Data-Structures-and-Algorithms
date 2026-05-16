# 1 se n tak ke saare numbers ka product (factorial) nikalo.

n = int(input("Enter a number to find the factorial: "))
fact = 1

for i in range(1,n+1):
    fact *= i

print(f"Factorial of {n} is {fact}")