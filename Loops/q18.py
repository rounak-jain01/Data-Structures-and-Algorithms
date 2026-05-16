# User se numbers lo tab tak jab tak 0 na enter kare, sum print karo at 
# the end.

isZero = True
s = 0

while isZero:
    n = int(input("Enter a number: "))
    if n != 0:
        isZero = False
    s+=n

print("The Sum is ",s)
