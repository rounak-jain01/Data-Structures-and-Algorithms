# String ke saare uppercase letters lowercase mein convert karo 
# without built-in lower(). 

val = "ABCDEF"
upp = ""

for i in val:
    upp += chr(ord(i) + 32)

print(upp)