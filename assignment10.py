#
# Assignment 10:
#
# Solve this problem from https://projecteuler.net/problem=4:
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
w = 0
for x in range(100,1000):
    for y in range(100,1000):
        z = x * y
        ztwo = list(str(z))
        ztwo.reverse()
        ztwo = ''.join(ztwo)
        if z == int(ztwo) and w < z:
             w = z
print(w)