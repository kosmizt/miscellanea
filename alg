def bezout(a, b):
        if b == 0:
                return 1, 0, a
        else:
                q = a//b
                r = a%b
                x, y, g = bezout(b, r)
                return y, x - q*y, g

#

from math import factorial
def pascal(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")

        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

        print()
        
