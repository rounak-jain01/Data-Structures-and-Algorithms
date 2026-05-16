# List mein se saare duplicate elements remove karo, order maintain 
# karo

def remove_dup(l):
    
    seen = set()
    result = []

    for i in l:
        if i not in seen:
            result.append(i)
            seen.add(i)

    return result

l = [1, 2, 1, 3, 2, 4, 5, 4]
print(remove_dup(l))