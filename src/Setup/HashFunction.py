from .PrimeNumberGenerator import miller_rabin_primality_test
import random
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

'''The Hash Function and the PRF parameters use byte format'''

''' Random key K'''
def generate_random_key():
    #  using 128 bit key
    key = bytes(get_random_bytes(16))

    return key

'''Random c'''
def generate_random_c(l):
    # size is adjusted for performance
    # (l) -> theoretical range
    c = random.getrandbits(4)
    return c

''''PRF Fk(x)'''

def pseudo_random_function_f(k, x):
    """Using AES-256 BlockCipher as a Practical PRF"""
    # from int to bytes
    x = ("{0:b}".format(x)).encode()

    cipher = AES.new(k, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(x, AES.block_size))

    # transforming f into binary
    ct_bytes = bin(int.from_bytes(ct_bytes, 'little'))
    ct_bytes = bytes(ct_bytes, 'utf-8')

    # transforming f into int
    ct_int = int.from_bytes(ct_bytes, 'little')

    # reducing bit size of f for performance reasons
    ct_final = int(str(ct_int)[:5])
    return ct_final

''' Hash Function Hk(x)'''

def hash_function(c, s, k):
    f = pseudo_random_function_f(k, s)
    h = c ^ f

    # checking if e is prime
    while not miller_rabin_primality_test(h):
        print("Not prime")
        s += 1
        f = pseudo_random_function_f(k, s)
        h = c ^ f
    else:
        # values used to double-check bit size of f and h
        h_bits = int.bit_length(h)
        f_bits = int.bit_length(f)
        print("Prime Hk(s) = " + str(h))

        return h, s
