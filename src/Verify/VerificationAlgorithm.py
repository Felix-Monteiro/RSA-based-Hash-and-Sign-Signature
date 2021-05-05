import math


def verification(i, l, es, o1, x, n, u, h, primality_test):
    #TODO Need to compute again values
    times_s = (2 * (math.ceil(math.log(i))))
    y = o1 ** times_s

    if not 0 < i < (2 ** l):
        print("ERROR: Rejected because i not correct")
    elif not primality_test:
        print("ERROR: Rejected because Hk(i) not a prime")
    elif (y ** es) % n == ((u ** x) * h) % n:
        print("Signature Verified!")
    else:
        print("ERROR: Rejected equality in mod N failed")

    return
