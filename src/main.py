from Setup import PrimeNumberGenerator
from Setup import BlumWilliamsTest


def setup():
    primes = PrimeNumberGenerator
    blum = BlumWilliamsTest

    while True:
        n = primes.prime_generator()  # generates N
        print("N = " + str(n))
        if blum.blum_integer_test(n):
            print("Is a Blum Integer")
            # calculate Quadratic residue
            return
        else:
            print("Not a Blum Integer\n Choosing New Primes...")


# def sign(sk, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    setup()
    # sign()
    # verify()
