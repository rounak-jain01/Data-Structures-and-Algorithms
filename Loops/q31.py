# List ka maximum aur minimum element loop se dhundo (max()/min() 
# mat use karo).

l = [1,5,7,3,2,88,0,6,3,2,4,8]
maxnum = l[0]
minnum = l[0]

for i in l:
    if maxnum < i:
        maxnum = i
    if minnum > i:
        minnum = i

print(maxnum,minnum)
    
