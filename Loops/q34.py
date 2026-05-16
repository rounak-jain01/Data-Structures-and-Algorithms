# List ke elements ko reverse order mein print karo without reverse().


def rev_list(l):
    newlist = []
    for i in range(len(l)-1,-1,-1):
        newlist.append(l[i])

    return newlist



l = [1,2,3,4,5]
print(rev_list(l))
