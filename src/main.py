import random
from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues
from Setup import HashFunction
from Setup import ChameleonHashFunction
from Setup import KeysGeneration
from Sign import SignerComputation
from Verify import VerificationAlgorithm


def setup(l, l_p):
    s = 0  # state counter
    security_param_l = 2 * l
    security_param_l_p = 2 * l_p

    primes = PrimeNumberGenerator
    qr = QuadraticResidues
    hash_function = HashFunction
    chameleon_hash = ChameleonHashFunction
    keys_generator = KeysGeneration

    print("=> Starting Setup Algorithm!")

    print("Generating new Secure Primes...\n")
    # generates N
    primes_rsa = primes.prime_generator(l, security_param_l)
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
    c = hash_function.generate_random_c(security_param_l)
    k = hash_function.generate_random_key()
    print("Random Key K = " + str(k) + " random parameter c = " + str(c))

    print("\n=====================================================")
    print("Publishing Parameters L from the Chameleon Hash Scheme...\n")
    primes_cha_hash = primes.prime_generator(l_p, security_param_l_p)
    p_ch = primes_cha_hash[0]
    q_ch = primes_cha_hash[1]
    n_ch = p_ch * q_ch

    e = chameleon_hash.random_e(p_ch, q_ch)
    j = chameleon_hash.random_j(n_ch)
    L = str(n_ch) + str(e) + str(j)  # random values used in CHF
    print("Parameters L:\ne = " + str(e) + " j = " + str(j) + " n = " + str(n_ch) + " " + str(int.bit_length(n_ch)))

    print("\n=====================================================")
    print("Building Public and Secret Keys...\n")
    pub_key = keys_generator.public_key(n, u, h, c, k, L)
    e_sec = keys_generator.random_e(security_param_l, p, q)
    sec_key = keys_generator.secret_key(p, q, e_sec)
    print("Public Key = " + pub_key + "\nSecret Key = " + str(sec_key))
    print("\n=====================================================")

    setup_parameters = s, sec_key, pub_key, j, e, n_ch, c, k, n, u, h
    return setup_parameters


def sign(rtn, m, l_p):
    s = rtn[0]
    s += 1  # incrementing s counter

    security_param_l_p = 2 * l_p
    chameleon_hash = ChameleonHashFunction
    hash_function = HashFunction
    signer_computation = SignerComputation
    primes = PrimeNumberGenerator

    print("=> Starting Sign Algorithm!")

    print("\n=====================================================")
    print("Calculating random r based on the Chameleon Hash Function...\n")
    r = chameleon_hash.random_r(security_param_l_p)
    print("r =" + str(r))

    print("\n=====================================================")
    print("Calculating x = ChamHash(M,r)\n")
    x = chameleon_hash.chameleon_hash_function(m, r, int(rtn[3]), int(rtn[4]), int(rtn[5]))
    x_bits = int.bit_length(x)
    print("x =" + str(x) + " " + str(x_bits))

    print("\n=====================================================")
    print("Getting a Prime Hk(s)...\n")
    k = rtn[7]  # random key k
    c = rtn[6]  # random c
    # checking if e is prime
    h_s = hash_function.hash_function(c, s, k)

    print("\n=====================================================")
    print("Computing B...\n")
    u = rtn[9]
    h = rtn[10]
    n = rtn[8]
    b = signer_computation.function_b(u, x, h, h_s[1], n)
    print("B = " + str(b))

    print("\n=====================================================")
    print("Signing...\n")
    es = h_s[0]
    signature = signer_computation.signature(b, es, r, h_s[1])
    print("Signature = " + str(signature))

    print("\n=====================================================")
    print("verification...\n")
    verification = VerificationAlgorithm
    o1= signature[0]
    verification.verification(h_s[1],32,es,o1,x,n,u,h,primes.miller_rabin_primality_test(es))


def main():
    security_parameter_lambda = 16  # 512 gives 1024 n bit size - 511
    security_parameter_lambda_p = 4
    security_parameter_lambda_p_p = 11  # 681 n bit cham_hash - 340 (2l/3)
    message = random.getrandbits(security_parameter_lambda_p)

    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    rtn = setup(security_parameter_lambda, security_parameter_lambda_p_p)
    sign(rtn, message, security_parameter_lambda_p_p)
    # verify()
    print("\n                                                 === End of Program ===")


if __name__ == '__main__':
    main()
