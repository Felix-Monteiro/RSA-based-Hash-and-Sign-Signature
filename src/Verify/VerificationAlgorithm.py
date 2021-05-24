import math


def verification(i, l, es, o1, x, n, u, h, primality_test):
    Y = (o1 ** (2 ** (math.ceil(math.log(i, 2))))) % n

    y_es = round(Y ** es) % n
    print("Y^e = " + str(y_es))

    u_x = ((u ** x) * h) % n
    print("u^x * h mod n = " + str(u_x))

    ''' Verification Tests '''
    if not i > 0 and i < (2 ** l):
        print("\nERROR: Rejected because i not correct")
    elif not primality_test:
        print("\nERROR: Rejected because Hk(i) not a prime")
    elif y_es == u_x:
        print("\nSignature Verified!")
        return True
    else:
        print("Signature Failed: Rejected equality in mod N failed\n" + "\nStaring new Parameters to retry Signing "
                                                                        "message...\n")
        return False
