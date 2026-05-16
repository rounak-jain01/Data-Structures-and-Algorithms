# Check Palindrome

def func(i,n):

    if i >= n//2:
        return True

    if s[i] != s[n-i-1]:
        return False
    return func(i+1,n)


s = "nitin"
print(func(0,len(s)))
