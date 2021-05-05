import math

def function_b(u, x, h, s, n):
    b = ((u ** x) * h) ** ((1 // 2) * math.ceil(math.log(s)))
    b = b % n
    return b

def signature(b, e, r, s):
    o = b**(1//e)
    return o,r,s