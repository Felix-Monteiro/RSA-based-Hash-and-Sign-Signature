import random
import sys
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
'''The Hash Function and the PRF parameters use byte format'''

''' Random key K'''
def generate_random_key():
    #  using 256 bit key
    key = bytes(get_random_bytes(32))

    return key

'''Random c'''
def generate_random_c(l):
    c = random.getrandbits(l)
    return c

''''PRF Fk(x)'''

def pseudo_random_function_f(k, x):
    """Using AES-256 BlockCipher"""
    x = ("{0:b}".format(x)).encode()  # from int to bytes
    cipher = AES.new(k, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(x, AES.block_size))

    return ct_bytes

''' Hash Function Hk(x)'''

def hash_function(c, f):
    # transforming f into binary
    mode = 'little'
    f = bin(int.from_bytes(f, 'little'))[2:]
    f = bytes(f, 'utf-8')
    f = int.from_bytes(f, mode)

    h = c ^ f

    return h
