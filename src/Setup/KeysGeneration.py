import math
import random

'''Concatenation of values that compose the Public Key'''
def public_key(n, u, h, c, k, L):
    pub_key = str(n) + str(u) + str(h) + str(c) + str(int.from_bytes(k, 'little')) + str(L)

    return pub_key

def random_e(p, q):
    phi_n = (p - 1) * (q - 1)
    lcm = phi_n // math.gcd(p - 1, q - 1)
    e = random.randint(2, lcm)

    # check_relatively_primes_to_e
    while math.gcd(e, phi_n) != 1 or math.gcd(e, lcm) != 1:
        e = random.randint(2, lcm)
    return e

'''Extended Euclidean Algorithm used to find the inverse of e'''
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def modular_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def secret_key(p, q, e):
    phi_n = (p - 1) * (q - 1)
    d = modular_inverse(e, phi_n)
    if (e * d) % phi_n == 1 % phi_n:
        return d
