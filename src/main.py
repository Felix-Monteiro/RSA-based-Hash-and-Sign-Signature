from Setup import PrimeNumberGenerator
from Setup import BlumWilliamsTest
from Setup import QuadraticResidues

def setup():
    primes = PrimeNumberGenerator
    blum = BlumWilliamsTest
    qr = QuadraticResidues

    while True:
        n = primes.prime_generator()  # generates N
        print("N = " + str(n))
        if blum.blum_integer_test(n):
            print("Is a Blum Integer")
            # calculate Quadratic residue
            qr.legendre_symbol(n)
            print(qr.legendre_symbol(n))
            return
        else:
            print("Not a Blum Integer\n Choosing New Primes...")


# def sign(sk, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    setup()
    # sign()
    # verify()
