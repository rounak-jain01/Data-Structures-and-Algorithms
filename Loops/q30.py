# String mein consecutive duplicate characters remove karo. (e.g. 
# 'aabbcc' → 'abc')

val = "abbbccddeeeee"
newval = val[0]
ind = 1

while (ind < len(val)):
    if val[ind] != val[ind - 1]:
        newval += val[ind]

    ind += 1



print(newval)