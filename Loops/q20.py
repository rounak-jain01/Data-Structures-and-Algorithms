# Inverted star pattern print karo (5 rows): ***** **** *** ** *

rows = 6

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("")