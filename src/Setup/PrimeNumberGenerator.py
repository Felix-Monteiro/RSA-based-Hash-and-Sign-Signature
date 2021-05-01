# Large Prime Generation for RSA Signature
import random

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


def random_prime_candidate(n):
    return random.randrange(1,n)


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


def prime_generator(l):
    p = coprime_checker(l)
    q = coprime_checker(l)

    # blum integer test and rabin miller
    while (p % 4) != 3 or miller_rabin_primality_test(p) != True:
        p = coprime_checker(l)

    while (q % 4) != 3 or miller_rabin_primality_test(q) != True or q == p:
        q = coprime_checker(l)

    phi_n = (p - 1) * (q - 1)
    if 2 ** l < phi_n < 2 ** (l + 2):
        print("Security Parameter l = " + str(l) + " and it is secure")
    else:
        print("Security Parameter l = " + str(l) + " and it is insecure")

    print("Secure Prime p = " + str(p))
    print("Secure Prime q = " + str(q) + "\n")
    return p, q
