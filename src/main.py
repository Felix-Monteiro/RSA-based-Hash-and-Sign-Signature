from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues
from Setup import HashFunction


def setup():
    security_parameter_l = 6  # bit size

    print("=> Starting Setup Algorithm!")
    primes = PrimeNumberGenerator
    qr = QuadraticResidues
    hash_function = HashFunction

    print("\n=====================================================")
    print("Generating new Secure Primes...\n")
    # generates N
    n = primes.prime_generator(security_parameter_l)
    print("Product of the two primes is...\nN = " + str(n) + "\n")

    print("\n=====================================================")
    print("Calculating two random different Quadratic Residues...\n")
    lqr = qr.get_random_qr(qr.jacobi_legendre_qr(n))
    u = lqr[0]  # First QR
    h = lqr[1]  # Second QR

    print("\n=====================================================")
    print("Getting Parameters K and c from the Hash Function...\n")
    c = hash_function.generate_random_c(security_parameter_l)
    k = hash_function.generate_random_key()
    print("Random Key K = " + str(k) + " random parameter c = " + str(c))


# def sign(sk, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    setup()
    # sign()
    # verify()
    print("\n                                                 === End of Program ===")
