from .PrimeNumberGenerator import miller_rabin_primality_test
import random
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

'''The Hash Function and the PRF parameters use byte format'''

''' Random key K'''
def generate_random_key():
    #  using 256 bit key
    key = bytes(get_random_bytes(16))

    return key

'''Random c'''
def generate_random_c(l):
    c = random.getrandbits(l)
    return c

''''PRF Fk(x)'''

def pseudo_random_function_f(k, x):
    """Using AES-256 BlockCipher"""
    mode = 'little'
    x = ("{0:b}".format(x)).encode()  # from int to bytes
    cipher = AES.new(k, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(x, AES.block_size))
    # transforming f into binary
    ct_bytes = bin(int.from_bytes(ct_bytes, 'little'))[124:]
    ct_bytes = bytes(ct_bytes, 'utf-8')
    # transforming f into int
    ct_int = int.from_bytes(ct_bytes, mode)
    return ct_int

''' Hash Function Hk(x)'''

def hash_function(c, s, k):
    s += 1
    f = pseudo_random_function_f(k, s)
    h = c ^ f
    # checking if e is prime
    while not miller_rabin_primality_test(h):
        print("not prime")
        s += 1
        f = pseudo_random_function_f(k, s)
        h = c ^ f
    else:
        x_bits = int.bit_length(h)
        print("Prime Hk(s) = " + str(h) + str(x_bits))
        return h, s
