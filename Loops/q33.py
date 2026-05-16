# List mein ek given element kitni baar aata hai count karo. 

def occ_count(l, num):
    count = 0
    for i in l:
        if i == num:
            count += 1

    return count

l = [1,2,1,1,2,4,4,2,1,5,6,1]
num = 1
print(occ_count(l,num))