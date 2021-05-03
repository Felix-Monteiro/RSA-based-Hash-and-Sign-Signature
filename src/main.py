import random
import sympy
from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues
from Setup import HashFunction
from Setup import ChameleonHashFunction
from Setup import KeysGeneration



def setup(l, l_p):
    s = 0  # state counter

    primes = PrimeNumberGenerator
    qr = QuadraticResidues
    hash_function = HashFunction
    chameleon_hash = ChameleonHashFunction
    keys_generator = KeysGeneration

    print("=> Starting Setup Algorithm!")

    print("Generating new Secure Primes...\n")
    # generates N
    primes_rsa = primes.prime_generator(l)
    p = primes_rsa[0]
    q = primes_rsa[1]
    print("p = " + str(p) + "\n")
    print("q = " + str(q) + "\n")

    n = p * q
    print("Product of the two primes is...\nN = " + str(n) + "\n")

    print("\n=====================================================")
    print("Calculating two random different Quadratic Residues...\n")
    lqr = qr.get_random_qr(n)
    u = lqr[0]  # First QR
    h = lqr[1]  # Second QR

    print("\n=====================================================")
    print("Getting Parameters K and c from the Hash Function...\n")
    c = hash_function.generate_random_c(l)
    k = hash_function.generate_random_key(l)
    print("Random Key K = " + str(k) + " random parameter c = " + str(c))

    print("\n=====================================================")
    print("Publishing Parameters L from the Chameleon Hash Scheme...\n")
    primes_cha_hash = primes.prime_generator(l_p)
    p_ch = primes_cha_hash[0]
    q_ch = primes_cha_hash[1]
    n_ch = p_ch * q_ch

    e = chameleon_hash.random_e(l_p, p_ch, q_ch)
    j = chameleon_hash.random_j(n_ch)
    L = str(n_ch) + str(e) + str(j)  # random values used in CHF
    print("Parameters L:\ne = " + str(e) + " j = " + str(j) + " n = " + str(n_ch))

    print("\n=====================================================")
    print("Building Public and Secret Keys...\n")
    pub_key = keys_generator.public_key(n, u, h, c, k, L)
    e_sec = keys_generator.random_e(l, p, q)
    sec_key = keys_generator.secret_key(p, q, e_sec)
    print("Public Key = " + pub_key + "\nSecret Key = " + str(sec_key))
    print("\n=====================================================")

    setup_parameters = s, sec_key, pub_key, j, e, n, c, k
    return setup_parameters


def sign(rtn, m, l_p):
    s = rtn[0]
    s += 1  # incrementing s counter

    chameleon_hash = ChameleonHashFunction
    hash_function = HashFunction

    print("=> Starting Sign Algorithm!")

    print("\n=====================================================")
    print("Calculating random r based on the Chameleon Hash Function...\n")
    r = chameleon_hash.random_r(l_p)
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
    e = hash_function.hash_function(c, f)
    while True:
        if not sympy.isprime(e):
            s += 1
            f = hash_function.pseudo_random_function_f(k, s)
            e = hash_function.hash_function(c, f)

        elif sympy.isprime(e):
            print(" prime" + str(e))
            return False


if __name__ == '__main__':
    security_parameter_l = 512  # 512 gives 1024 n bit size
    security_parameter_l_p = 32
    security_parameter_l_p_p = 128

    m = random.getrandbits(security_parameter_l_p)

    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    rtn = setup(security_parameter_l, security_parameter_l_p_p)
    sign(rtn, m, security_parameter_l_p_p)
    # verify()
    print("\n                                                 === End of Program ===")
