import random
import math

'''Random e'''
def generate_random(l):
    r = ""
    encoding = 'utf8'
    # Iterate over the range [0, l - 1]
    for i in range(l):
        # Generate the random number
        num = random.randint(0, 1)

        r += str(num)

    r = bytes(r, encoding)
    return r


def check_relatively_primes(l, r, p, q):
    encoding = 'utf8'
    e = int.from_bytes(r, "big")
    phi_n = (p - 1) * (q - 1)

    while math.gcd(e, phi_n) != 1:
        ep = generate_random(l)
        e = int.from_bytes(ep, "big")

    return e


'''Random j'''
def random_j(n):
    j = random.randint(0, (n - 1) % n)
    return j


''' CHF Public Key '''
def public_key(n, e, j):
    pub_key = str(n) + str(e) + str(j)
    return pub_key

'''Function Trapdoor'''
def value_d(e, p, q):
    phi_n = (p - 1) * (q - 1)
    for d in range(phi_n):
        if (e * d) % phi_n == 1 % phi_n:
            return d


'''Factorization of N'''
def trapdoor(n, d):
    n_factorization = ""
    for i in range(1, n + 1):
        if n % i == 0:
            n_factorization += str(i)

    trap_d = n_factorization + str(d)
    return trap_d

# TODO declare the actual Chameleon hash function
