import random
from src import main

""" Finds all the Quadratic Residues for a given N """
def legendre_symbol(n):
    a = 0
    qr_list = []

    while a <= (n - 1) // 2:
        ls = pow(a, (n - 1) // 2, n)
        if ls == 1 % n:
            print("QR found : " + str(a))
            qr_list.append(a)
            a += 1
        else:
            #print("Legendre Symbol Rule Failed")
            a += 1

    print("The Quadratic Residues of " + str(n) + " are : " + str(qr_list))
    return qr_list


""" Picks two random QR from the list of QRs of N """
def get_random_qr(qr_list):
        qr_1 = int(random.choice(qr_list))
        qr_2 = int(random.choice(qr_list))

        # Assuming that the QRs cannot be the same
        if qr_1 == qr_2:
            qr_2 = random.choice(qr_list)

        else:
            print("QR 1 = " + str(qr_1) + "\n" + "QR 2 = " + str(qr_2))
            return qr_1, qr_2