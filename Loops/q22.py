# Multiplication table 1 se 5 tak (5x5 grid) print karo. 

grid = 6

for i in range(1,grid+1):
    for j in range(1,grid+1):
        print(j*i,end=" ")
    print("")