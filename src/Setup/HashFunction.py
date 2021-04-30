import random
import hmac
import hashlib

'''The Hash Function and the PRF parameters use byte format'''

''' Random key K'''

def generate_random_key():
    k = ""
    sha256 = 250  # using SHA256 parameters
    encoding = 'utf8'

    # Iterate over the range
    for i in range(sha256):
        # Generate the random number
        num = random.randint(0, 1)

        k += str(num)

    key_bytes = ''.join(format(ord(i), '08b') for i in k)
    return bytes(key_bytes, encoding)


''''Random c'''

def generate_random_c(l):
    encoding = 'utf8'
    c = random.randint(0,l)
    c_bytes = c.to_bytes(l, 'big')
    return c_bytes

''''PRF Fk(x)'''

def pseudo_random_function_f(k, x):
    encoding = 'utf8'
    signature = hmac.new(k, bytes(x), hashlib.sha256).hexdigest()
    sign_bytes = ''.join(format(ord(i), '08b') for i in signature)

    return bytes(sign_bytes, encoding)


''' Hash Function Hk(x)'''

def hash_function(c, f):
    mode = 'little'
    h = int.from_bytes(c, mode) ^ int.from_bytes(f, mode)

    return h

# TODO c is very small compared with f so the xor will not do much

