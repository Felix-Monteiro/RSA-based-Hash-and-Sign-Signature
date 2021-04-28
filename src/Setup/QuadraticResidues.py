import random

import libnum

""" Finds all the Quadratic Residues for a given N """


def jacobi_legendre_qr(n):
    a = 1
    qr_list = []

    while a <= n - 1:  # (n - 1) // 2
        ls = pow(a, (n - 1) // 2, n)  # manual legendre symbol
        rtn = libnum.jacobi(a, n)
        if rtn == 1 and a ** 2 % n == a**2:
            #print("QR found : " + str(a))
            qr_list.append(a)
            a += 1
        else:
            a += 1

    print("The Modulus N = " + str(n) + " has: " + str(len(qr_list)) + " Quadratic Residues in [1,N-1]")
    return qr_list


""" Picks two random QR from the list of QRs of N """


def get_random_qr(qr_list):
    qrs = random.sample(qr_list, 2)
    qr_1 = qrs[0]
    qr_2 = qrs[1]

    print("[QR 1] u = " + str(qr_1) + "\n" + "[QR 2] h = " + str(qr_2))
    return qr_1, qr_2

