# Check karo ki string palindrome hai ya nahi using loop.


val = "nitin"
s = 0
e = len(val) - 1
flag = True

while s < e:
    if val[s] != val[e]:
        flag = False
        break

    s += 1
    e -= 1

if flag:
    print(f"{val} is Palindrome.")
else:
    print(f"{val} is not Palindrome")


        
