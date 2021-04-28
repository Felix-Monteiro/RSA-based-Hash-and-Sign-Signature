from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues
from Setup import HashFunction
from Setup import ChameleonHashFunction


def setup():
    security_parameter_l = 10  # bit size
    m = 1234  # message

    print("=> Starting Setup Algorithm!")
    primes = PrimeNumberGenerator
    qr = QuadraticResidues
    hash_function = HashFunction
    chameleon_hash = ChameleonHashFunction

    print("\n=====================================================")
    print("Generating new Secure Primes...\n")
    # generates N
    p = primes.prime_generator(security_parameter_l)[0]
    q = primes.prime_generator(security_parameter_l)[1]
    n = p * q
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

    h = chameleon_hash.chameleon_hash_function(m, chameleon_hash.random_r(security_parameter_l),
                                               chameleon_hash.random_j(n),
                                               chameleon_hash.random_e(security_parameter_l, p, q), n)

    print(str(h))


# def sign(sk, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    setup()
    # sign()
    # verify()
    print("\n                                                 === End of Program ===")
