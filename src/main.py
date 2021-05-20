import os
import random
from Setup import PrimeNumberGenerator
from Setup import QuadraticResidues
from Setup import HashFunction
from Setup import ChameleonHashFunction
from Setup import KeysGeneration
from Sign import SignerComputation
from Verify import VerificationAlgorithm



def setup(l, l_p_p):
    primes = PrimeNumberGenerator
    qr = QuadraticResidues
    hash_function = HashFunction
    chameleon_hash = ChameleonHashFunction
    keys_generator = KeysGeneration

    s = 0  # state counter
    """These two security values are merely used for security checks"""
    security_param_l = 2 * l
    security_param_l_p_p = 2 * l_p_p

    print("=> Starting Setup Algorithm!")

    print("\n=====================================================")
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
    primes_cha_hash = primes.prime_generator(l_p_p, security_param_l_p_p)
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
    e_sec = keys_generator.random_e(p, q)
    sec_key = keys_generator.secret_key(p, q, e_sec)
    print("Public Key = " + pub_key + "\nSecret Key = " + str(sec_key))
    print("\n=====================================================")

    setup_parameters = s, sec_key, pub_key, j, e, n_ch, c, k, n, u, h
    return setup_parameters


def sign(rtn, m, l, l_p):
    chameleon_hash = ChameleonHashFunction
    hash_function = HashFunction
    signer_computation = SignerComputation
    primes = PrimeNumberGenerator
    verification = VerificationAlgorithm

    s = rtn[0]
    s += 1  # incrementing s counter

    security_param_l_p = 2 * l_p

    print("=> Starting Sign Algorithm!")

    print("\n=====================================================")
    print("Calculating random r based on the Chameleon Hash Function...\n")
    r = chameleon_hash.random_r(security_param_l_p)
    print("r =" + str(r))

    print("\n=====================================================")
    print("Calculating x = ChamHash(M,r)...\n")
    j = int(rtn[3])
    e = int(rtn[4])
    n_ch = int(rtn[5])
    x = chameleon_hash.chameleon_hash_function(m, r, j, e, n_ch)
    # x is being adjusted for performance
    x_final = int(str(x)[:2])
    x_bits = int.bit_length(x)
    print("x =" + str(x) + ", bit_size = " + str(x_bits))

    print("\n=====================================================")
    print("Getting a Prime Hk(s)...\n")
    k = rtn[7]  # random key k
    c = rtn[6]  # random c
    # generating es until Hk(s)=es is prime
    hash_k_of_s = hash_function.hash_function(c, s, k)

    print("\n=====================================================")
    print("Computing B...\n")
    u = rtn[9]
    h = rtn[10]
    n = rtn[8]
    s = hash_k_of_s[1]
    b = signer_computation.function_b(u, x_final, h, s, n)
    print("B = " + str(b))

    print("\n=====================================================")
    print("Signing...\n")
    es = hash_k_of_s[0]
    signature = signer_computation.signature(b, es, r, s)
    o1 = signature[0]
    m_signed = "(" + str(o1) + ", " + str(signature[1]) + ", " + str(signature[2]) + ")"
    print("Signature = " + str(m_signed))

    print("\n=====================================================")
    print("Verification...\n")
    vrf = verification.verification(s, l, es, o1, x, n, u, h, primes.miller_rabin_primality_test(es))
    return vrf

def success_rate():
    security_parameter_lambda = 15  # 512 gives 1024 n bit size - 511 15
    security_parameter_lambda_p = 2
    security_parameter_lambda_p_p = 9  # 681 n bit cham_hash - 340 (2l/3) 9
    message = random.getrandbits(security_parameter_lambda_p)
    validated = 0
    failed = 0
    for x in range(100):
        print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
        rtn = setup(security_parameter_lambda, security_parameter_lambda_p_p)
        sin = sign(rtn, message, security_parameter_lambda, security_parameter_lambda_p_p)
        # verify()
        print("\n                                                 === End of Program ===")
        if sin:
            validated += 1
        else:
            failed += 1

    os.system('clear')
    print("Validated :" + str(validated))
    print("Failed :" + str(failed))

def main():
    security_parameter_lambda = 15  # 512 gives 1024 n bit size - 511 15
    security_parameter_lambda_p = 2
    security_parameter_lambda_p_p = 9  # 681 n bit cham_hash - 340 (2l/3) 9
    message = random.getrandbits(security_parameter_lambda_p)
    print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
    rtn = setup(security_parameter_lambda, security_parameter_lambda_p_p)
    sin = sign(rtn, message, security_parameter_lambda, security_parameter_lambda_p_p)
    print("\n                                                 === End of Program ===")

    while not sin:
        print("\n                             === Hash-and-Sign Signature under the RSA Standard Assumptions ===\n")
        rtn = setup(security_parameter_lambda, security_parameter_lambda_p_p)
        sin = sign(rtn, message, security_parameter_lambda, security_parameter_lambda_p_p)
        # verify()
        print("\n                                                 === End of Program ===")


if __name__ == '__main__':
    main()
