# Number pattern print karo: 1 1 2 1 2 3 1 2 3 4

rows = 5

for i in range(0,rows+1):
    for j in range(0,i):
        print(j+1,end=" ")
    print()