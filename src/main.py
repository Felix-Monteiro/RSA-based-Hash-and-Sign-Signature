from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues

def setup():
    primes = PrimeNumberGenerator
    qr = QuadraticResidues

    while True:
        # generates N
        print("Generating new Secure Primes...")
        n = primes.prime_generator()
        print("N = " + str(n))

        # calculate the 2 random different Quadratic residue
        lqr = qr.get_random_qr(qr.legendre_symbol(n))
        u = lqr[0]  # First QR
        h = lqr[1]  # Second QR

        return False



# def sign(sk, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    setup()
    print("End of Program")
    # sign()
    # verify()
