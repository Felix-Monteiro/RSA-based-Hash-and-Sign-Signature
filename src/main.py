from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues
from Setup import HashFunction
from Setup import ChameleonHashFunction
from Setup import KeysGeneration
import sympy


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

    print("\n=====================================================")
    print("Publishing Parameter L from the Chameleon Hash Scheme...\n")
    e = str(chameleon_hash.random_e(l, p, q))
    j = str(chameleon_hash.random_j(n))
    L = str(n) + e + j  # random values used in CHF

    print("\n=====================================================")
    print("Building Public and Secret Keys...\n")
    pub_key = keys_generator.public_key(n, u, h, c, k, L)
    sec_key = keys_generator.secret_key(n)
    print("Public Key = " + pub_key + "\nSecret Key = " + str(sec_key))
    print("\n=====================================================")

    setup_parameters = s, sec_key, pub_key, j, e, n, c, k
    return setup_parameters


def sign(rtn, m, l):
    s = rtn[0]

    s += 1  # incrementing s counter
    chameleon_hash = ChameleonHashFunction
    hash_function = HashFunction

    print("=> Starting Sign Algorithm!")

    print("\n=====================================================")
    print("Calculating random r based on the Chameleon Hash Function...\n")
    r = chameleon_hash.random_r(l)
    print("r =" + str(r))

    print("\n=====================================================")
    print("Calculating x = ChamHash(M,r)\n")
    x = chameleon_hash.chameleon_hash_function(m, r, int(rtn[3]), int(rtn[4]), int(rtn[5]))
    print("x =" + str(x))

    print("\n=====================================================")
    print("Getting a Prime Hk(s)...\n")
    k = rtn[7]  # random key k
    c = rtn[6]  # random c
    # checking if e is prime
    f = hash_function.pseudo_random_function_f(k, s)
    e = hash_function.hash_function(rtn[6], f)
    while not sympy.isprime(e):
        s += 1
        f = hash_function.pseudo_random_function_f(k, s)
        e = hash_function.hash_function(c, f)
        print("not prime" + str(e))




if __name__ == '__main__':
    security_parameter_l = 10  # bit size
    m = 2345

    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    rtn = setup(security_parameter_l)
    sign(rtn, m, security_parameter_l)
    # verify()
    print("\n                                                 === End of Program ===")
