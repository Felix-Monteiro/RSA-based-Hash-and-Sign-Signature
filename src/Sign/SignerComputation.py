import math


def function_b(u, x, h, s, n):
    # TODO the square root does not seem to be well computed along with the multiplication
    s = math.ceil(math.log(s, 2))
    e = (1 / 2) ** s
    b = (((u ** x) * h) ** int(e)) % n   # dúvida se o valor e deve ser int ou não

    return b


def signature(b, es, r, s):
    o = b ** (1 / es)

    return o, r, s
