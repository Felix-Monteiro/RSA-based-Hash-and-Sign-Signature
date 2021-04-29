from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues
from Setup import HashFunction
from Setup import ChameleonHashFunction
from Setup import KeysGeneration


def setup(l):
    s = 0  # state counter

    primes = PrimeNumberGenerator
    qr = QuadraticResidues
    hash_function = HashFunction
    chameleon_hash = ChameleonHashFunction
    keys_generator = KeysGeneration

    print("=> Starting Setup Algorithm!")

    print("\n=====================================================")
    print("Generating new Secure Primes...\n")
    # generates N
    p = primes.prime_generator(l)[0]
    q = primes.prime_generator(l)[1]
    n = p * q
    print("Product of the two primes is...\nN = " + str(n) + "\n")

    print("\n=====================================================")
    print("Calculating two random different Quadratic Residues...\n")
    lqr = qr.get_random_qr(qr.jacobi_legendre_qr(n))
    u = lqr[0]  # First QR
    h = lqr[1]  # Second QR

    print("\n=====================================================")
    print("Getting Parameters K and c from the Hash Function...\n")
    c = hash_function.generate_random_c(l)
    k = hash_function.generate_random_key()
    print("Random Key K = " + str(k) + " random parameter c = " + str(c))
    # TODO the L parameters must be checked with the Professor
    print("\n=====================================================")
    print("Publishing Parameter L from the Chameleon Hash Scheme...\n")
    e = str(chameleon_hash.random_e(l, p, q))
    j = str(chameleon_hash.random_j(n))
    L = e + j  # random values used in CHF

    print("\n=====================================================")
    print("Building Public and Secret Keys...\n")
    pub_key = keys_generator.public_key(n, u, h, c, k, L)
    sec_key = keys_generator.secret_key(n)
    print("Public Key = " + pub_key + "\nSecret Key = " + str(sec_key))
    print("\n=====================================================")

    return s, sec_key, pub_key


# def sign(sec_key, s, m):


# def verify(pk, m, o):


if __name__ == '__main__':
    security_parameter_l = 10  # bit size

    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    setup(security_parameter_l)
    # sign()
    # verify()
    print("\n                                                 === End of Program ===")
