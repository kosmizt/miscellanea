def bezout(a, b):
        if b == 0:
                return 1, 0, a
        else:
                q = a//b
                r = a%b
                x, y, g = bezout(b, r)
                return y, x - q*y, g
