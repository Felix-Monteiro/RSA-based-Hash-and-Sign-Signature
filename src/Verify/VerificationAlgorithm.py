import math


def verification(i, lamda, es, o1, x, n, u, h, test):
    if not 0 < i < (2 ** lamda):
        print("rejected1")
        return
    if not test:
        print("rejected2")
        return
    y = o1 ** (2 * (math.ceil(math.log(i))))

    if (y ** es) % n == ((u ** x) * h) % n:
        print("verified")
    else:
        print("reject3")

    return
