import random
import Crypto.Util.number

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

'''Manual Prime number generation'''
def random_prime_candidate(n):
    # (n-1) + (1 << (n-1)) -> precise bit size
    return random.getrandbits(n)

'''Automatic Prime number generation'''
def random_prime_generator(n):
    return Crypto.Util.number.getPrime(n, Crypto.Random.get_random_bytes)

def coprime_checker(n):
    """ Generate a prime candidate divisible by first primes list"""
    while True:
        # Obtain a random number
        pc = random_prime_candidate(n)

        # Check if it is co prime with the first primes list
        for divisor in first_primes_list:
            # if it is perfectly divisible then test failed
            if pc % divisor == 0 and divisor ** 2 <= pc:
                break
        else:
            return pc


def miller_rabin_primality_test(mrc):
    max_divisions_by_two = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        max_divisions_by_two += 1
    assert (2 ** max_divisions_by_two * ec == mrc - 1)

    def trial_composite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(max_divisions_by_two):
            if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

    # Set number of trials here
    number_of_rabin_trials = 20

    # nr of iterations of Rabin Miller Primality test
    for i in range(number_of_rabin_trials):
        round_tester = random.randrange(2, mrc)
        if trial_composite(round_tester):
            return False
    return True

def safe_prime_parameters_gen(l):
    """Sophie Germain Primes"""

    """Safe Prime P"""
    p_candidate = random_prime_generator(l)
    p = (2 * p_candidate) + 1
    # blum integer test and rabin miller
    while not miller_rabin_primality_test(p) or (p % 4) != 3:
        p_candidate = random_prime_generator(l)
        p = (2 * p_candidate) + 1

    """Safe Prime q"""
    q_candidate = random_prime_generator(l)
    q = 2 * q_candidate + 1
    # blum integer test and rabin miller
    while not miller_rabin_primality_test(q) or (q % 4) != 3 or p == q:
        q_candidate = random_prime_generator(l)
        q = 2 * q_candidate + 1

    return p, q


def prime_generator(l):
    safe_primes = safe_prime_parameters_gen(l)
    p = safe_primes[0]
    q = safe_primes[1]

    phi_n = (p - 1) * (q - 1)

    # TODO this verification is never secure, what is l ?
    #  WIKI: the security parameter l denotes the length in bits of the modulus n;
    if (2 ** l) > phi_n or phi_n > (2 ** (l + 2)):
        print("Prime is insecure")
    else:
        print("Prime is secure")

    return p, q
