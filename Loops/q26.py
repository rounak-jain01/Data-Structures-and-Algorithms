# Ek string mein kitne vowels hain count karo.
s = "aeiou"
cnt = 0
for i in s:

    if i in "aeiouAEIOU":
        print(i)
        cnt += 1

print(f"Count of Vowels in {s} is {cnt}")