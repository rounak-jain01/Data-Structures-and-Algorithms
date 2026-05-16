# Bina multiplication operator use kiye, loop se A × B nikalo.

def mul_loop(a,b):
    total = 0
    for i in range(1,a+1):
        total += b

    print(total)

mul_loop(4,5)
    