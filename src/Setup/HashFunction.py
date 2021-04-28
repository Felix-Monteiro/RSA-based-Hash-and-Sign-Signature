import random
import hmac
import hashlib

'''The Hash Function and the PRF parameters use byte format'''

''' Random key K'''

def generate_random_key():
    k = ""
    sha256 = 256  # using SHA256 parameters
    encoding = 'utf8'

    # Iterate over the range
    for i in range(sha256):
        # Generate the random number
        num = random.randint(0, 1)

        k += str(num)

    return bytes(k, encoding)


''''Random c'''

def generate_random_c(l):
    c = ""
    encoding = 'utf8'
    # Iterate over the range [0, l - 1]
    for i in range(l):
        # Generate the random number
        num = random.randint(0, 1)

        c += str(num)

    return bytes(c, encoding)


''''PRF Fk(x)'''

def pseudo_random_function_f(k, x):
    encoding = 'utf8'

    signature = hmac.new(k, bytes(x), hashlib.sha256).hexdigest()
    sign_bytes = ''.join(format(ord(i), '08b') for i in signature)

    return bytes(sign_bytes, encoding)

''' Hash Function Hk(x)'''

def hash_function(c, f):
    encoding = 'utf8'

    h = int(c, 2) ^ int(f, 2)

    return bytes('{0:b}'.format(h), encoding)

# TODO  check if prime latter in Sign()
# c = hash_function(generate_random_c(6),pseudo_random_function_f(generate_random_key(),2))
# print(int.from_bytes(c, 'little'))
