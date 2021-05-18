import math

def function_b(u, x, h, s, n):
    # TODO Values need to be small
    s = math.ceil(math.log(s, 2))
    e = (1 / 2) ** s
    b = (((u ** x) * h) ** e) % n
    return b


def signature(b, es, r, s):
    o = b ** (1 / es)

    return o, r, s
