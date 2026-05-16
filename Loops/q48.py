# Loop se check karo ki koi number perfect hai ya nahi (sum of factors = 
# number, e.g. 6).
import math
def perfect_num(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        print(total)
        print("Perfect Num")
    else:
        print("Not Perfect")

perfect_num(6)
