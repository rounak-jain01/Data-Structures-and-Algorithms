# List mein pehla negative number dhundo aur uske baad loop band 
# karo.

l = [1,4,6,-2,5,6,-9,6,9,5,32,6,4]

for i in l:
    if i < 0:
        print(i)
        break
    print(i,end=" ")