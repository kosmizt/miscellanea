def bezout(a, b, top_level=True):
    """the minimal pair of bezout coefficients (they are infinite!)
    ax + by = gcd(a, b);
    (x + k*b/gcd, y - k*a/gcd)
    a(x + k*b/gcd) + b(y - k*a/gcd) = gcd"""
    if b == 0:
        x, y, g = 1, 0, a
        print(f"{a}*{x} + {b}*{y} = {g}")
        return x, y, g
    else:
        q = a // b
        r = a % b
        print(f"{a} = {b}*{q} + {r} (q = {q}, r = {r})")
        x, y, g = bezout(b, r, top_level=False)
        x, y = y, x - q * y
        print(f"{a}*{x} + {b}*{y} = {g}")
        
        if top_level:
            print(f"gcd = {g}")
            print(f"general solution: ({x} + k*{b//g}, {y} - k*{a//g})")
            print(f"general form: {b}({y}-{a//g}k) + {a}({x}+{b//g}k) = {g}")

        return x, y, g
    
#

from math import factorial
def pascal(n):
    """pascal's triangle"""
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")

        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

        print()
