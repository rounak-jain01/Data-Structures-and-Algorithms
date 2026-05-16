# 1 se 30 tak sirf prime numbers print karo (inner loop mein break use karo).

 
for i in range(1,31):
    isPrime = True
    for j in range(2,i):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        print(i,end=" ")





