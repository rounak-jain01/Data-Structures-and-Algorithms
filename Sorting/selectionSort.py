

def selectionSort(l):
    for i in range(len(l)-1):
        mini = i
        # print(mini)
        for j in range(i,len(l)):
            if l[j] < l[mini]:
                mini = j
                # print(mini)

        l[i],l[mini] = l[mini],l[i]

    return l

l = [13,46,24,52,20,9,3]
print(selectionSort(l))
