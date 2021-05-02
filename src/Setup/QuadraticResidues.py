import random
import libnum

""" Finds all the Quadratic Residues for a given N """

def jacobi_legendre_qr(n):
    while True:  # (n - 1) // 2
        a = random.randint(2, n)
        rtn = libnum.jacobi(a, n)
        if rtn == 1 and a ** 2 % n == a ** 2:
            return a


""" Picks two random QR from the list of QRs of N """

def get_random_qr(n):

    qr_1 = jacobi_legendre_qr(n)
    qr_2 = jacobi_legendre_qr(n)
    while qr_1 == qr_2:
        qr_1 = jacobi_legendre_qr(n)
        qr_2 = jacobi_legendre_qr(n)

    print("[QR 1] u = " + str(qr_1) + "\n" + "[QR 2] h = " + str(qr_2))
    return qr_1, qr_2
