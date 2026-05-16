# Digits ka sum nikalo (e.g. 1234 → 10) while loop se.

n = int(input("Enter a number to find it's Sum: "))
s = 0
while (n!=0):
    s += n % 10
    n //= 10

print(f"The sum is {s}")