# Hollow square pattern print karo (N=5): sirf border mein * baaki 
# spaces.

rows = 6

for i in range(0,rows+1):
    for j in range(0,rows+1):
        if i == 0 or i == rows :
            print("*", end=" ")
        elif j == 0 or j == rows:
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print()