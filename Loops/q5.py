# 1 se n tak ke saare numbers ka sum nikalo. (n user se lo)
n = int(input("Enter a number: "))

sum = 0
for i in range(1,n+1):
    sum += i

print(f"Sum from 1 - {n} is: {sum} ")