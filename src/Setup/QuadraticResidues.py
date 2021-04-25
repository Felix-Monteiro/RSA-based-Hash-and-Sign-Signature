import random


def legendre_symbol(n):
    a = 2
    while True:
        # random number between 1 and n//2
        ls = pow(a, (n - 1) // 2, n)
        if ls == 1 % n:
            print("QR is: " + str(a))
            return a
        else:
            print("ls failed")
            a += 1
