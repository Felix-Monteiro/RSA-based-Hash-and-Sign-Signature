import math
import random
import libnum

'''Jacobi Calculation may provide non quadratic values - NOT USED'''
def jacobi_legendre_qr(n):
    a = random.randint(1, math.floor(n // 2))
    while True:
        rtn = libnum.jacobi(a, n)
        if rtn == 1:
            return a
        else:
            a -= 1

""" Picks two random QR from the list of QRs of N """
def get_random_qr(n):
    # sizes are adjusted for performance
    # (n-1) -> theoretical range
    u = random.randint(2, (n-1)/2)
    h = random.randint(2, (n-1)/2)

    qr_u = pow(u, 2, n)
    qr_h = pow(h, 2, n)

    while u == h:
        u = random.randint(2, (n - 1) / 2)
        h = random.randint(2, (n - 1) / 2)

        qr_u = pow(u, 2, n)
        qr_h = pow(h, 2, n)
    print("[QR 1] u = " + str(qr_u) + "\n" + "[QR 2] h = " + str(qr_h))

    return qr_u, qr_h
