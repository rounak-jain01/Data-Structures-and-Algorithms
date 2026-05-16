# User se number lo aur while loop se uska reverse print karo (digits ek-ek karke).

n = int(input("Please Enter a number: "))
temp = 0
num = 0
while n != 0:
    temp = n % 10
    num = (num * 10) + temp
    n //= 10

print(f"Reverse of number is {num}")



