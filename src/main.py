from Setup import PrimeNumberGenerator
from Setup import BlumWilliamsTest
from Setup import QuadraticResidues

def setup():
    primes = PrimeNumberGenerator
    blum = BlumWilliamsTest
    qr = QuadraticResidues

    while True:
        # generates N
        print("Generating new Secure Primes...")
        n = primes.prime_generator()
        print("N = " + str(n))

        # blum number check
        if blum.blum_integer_test(n):
            print(str(n) + " Is a Blum Integer")
            # calculate the 2 random Quadratic residue
            lqr = qr.get_random_qr(qr.legendre_symbol(n))

            qr1 = int(lqr[0])  # First QR
            qr2 = int(lqr[1])  # Second QR

            return False
        else:
            print("ERROR: Not a Blum Integer")


# def sign(sk, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    setup()
    print("End of Program")
    # sign()
    # verify()
