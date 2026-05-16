# Pyramid pattern print karo (5 rows):     *    ***   *****  *******  *********

n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * (2*i - 1))