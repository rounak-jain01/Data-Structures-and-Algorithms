# 1 se 500 tak ke saare Armstrong numbers print karo.

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


for i in range(1,501):
    num = check_armstrong(i)
    if num == i:
        print(num)