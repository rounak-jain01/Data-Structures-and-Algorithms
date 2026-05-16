# Ek number n ka table print karo (1 se 10 tak).

n = int(input("Enter a number to print it's table: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")