# Ek number ka digit reversal karo using loop (e.g. 1234 → 4321).]

def digit_reserse(n):
    sumvar = 0
    while n != 0:
        sumvar = (sumvar * 10) + n % 10
        n //= 10

    return sumvar

n = 143
print(digit_reserse(n))