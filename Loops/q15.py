# 1 se 20 tak print karo lekin 3 ke multiples skip karo (continue use 
# karo). 

for i in range(1,21):
    if (i%3==0):
        continue
    print(i, end=" ")