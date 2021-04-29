import random
import math

'''Random e'''

def random_e(l, p, q):
    """security parameter l'' = l^2"""
    e = random.randint(0, l**2)
    phi_n = (p - 1) * (q - 1)

    # check_relatively_primes_to_e
    while math.gcd(e, phi_n) != 1:
        e = random.randint(1, l**2)

    return e


'''Random j'''
def random_j(n):
    j = random.randint(1, n - 1)
    return j

'''Random r'''
def random_r(l):
    """security parameter l'' = l^2"""
    r = random.randint(1, l**2)
    return r


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

def chameleon_hash_function(m, r, j, e, n):
    h = ((j ** m) * (int(r) ** e) % n)

    return h
