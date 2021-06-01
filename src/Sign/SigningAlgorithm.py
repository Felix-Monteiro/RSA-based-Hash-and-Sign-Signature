import math


def function_b(u, x, h, s, n):
    s = math.ceil(math.log(s, 2))
    b = pow(pow(u, x) * h, round(1 / 2) ** s, n)

    return b


def signature(b, es, r, s):
    o = pow(b, (1 / es))

    return o, r, s
