# List ke saare elements ka average nikalo

def list_avg(l):
    total = 0
    for i in l:
        total += i
    
    return (total / len(l))

l = [1,2,3,4,55]
print(list_avg(l))