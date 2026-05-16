# Do lists merge karo bina zip() ya + use kiye — loop se.

def merge_list(l1,l2):
    l3 = []
    for i in range(0,len(l1)):
        l3.append(l1[i])

    for i in range(0,len(l2)):
        l3.append(l2[i])

    print(l3)

merge_list([1,2,3],[4,5,6])