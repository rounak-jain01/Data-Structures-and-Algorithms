# String ko reverse karo using loop (slicing mat use karo).

s = "ankit"
rev = ""
for i in range(len(s)-1,-1,-1):
    rev += s[i]

print(rev)