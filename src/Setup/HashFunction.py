import random
from cryptography.fernet import Fernet

'''The Hash Function and the PRF parameters use byte format'''

''' Random key K'''
def generate_random_key(l):
    #  using 128 bit key
    key = Fernet.generate_key()

    return key

'''Random c'''
def generate_random_c(l):
    c = random.getrandbits(l)
    return c

''''PRF Fk(x)'''

def pseudo_random_function_f(k, x):
    """Using AES-128 BlockCipher"""
    x = ("{0:b}".format(x)).encode()   # from int to bytes
    f = Fernet(k)
    ciphertext = f.encrypt(x)

    return ciphertext

''' Hash Function Hk(x)'''

def hash_function(c, f):
    mode = 'little'
    f = int.from_bytes(f, mode)
    h = c ^ f

    return h

# TODO c is very small compared with f so the xor will not do much