from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues

def setup():
    print("=> Starting Setup Algorithm!\n")
    primes = PrimeNumberGenerator
    qr = QuadraticResidues

    while True:

        print("Generating new Secure Primes...\n")
        # generates N
        n = primes.prime_generator()
        print("Product of the two primes is...\nN = " + str(n) + "\n")

        # calculate the 2 random different Quadratic residue
        lqr = qr.get_random_qr(qr.jacobi_legendre_qr(n))
        u = lqr[0]  # First QR
        h = lqr[1]  # Second QR

        return False



# def sign(sk, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    setup()
    # sign()
    # verify()
    print("\n                                                 === End of Program ===")
