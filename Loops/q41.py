def length(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


def check_armstrong(n):
    size = length(n)
    temp = n
    tempv = 0

    while temp != 0:
        digit = temp % 10
        tempv += digit ** size
        temp //= 10

    return tempv


n = 153
result = check_armstrong(n)

if n == result:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")