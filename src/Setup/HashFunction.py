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
    c = random.randint(0, l)

    return c


''''PRF Fk(x)'''

def pseudo_random_function_f(k, x):
    encoding = 'utf8'
    signature = hmac.new(k, bytes(x), hashlib.sha256).hexdigest()
    sign_bytes = ''.join(format(ord(i), '08b') for i in signature)

    return bytes(sign_bytes, encoding)

''' Hash Function Hk(x)'''

def hash_function(c, f):
    mode = 'little'
    h = c ^ int.from_bytes(f,mode)

    return h

# TODO  check if prime latter in Sign()
#c = hash_function(generate_random_c(6),pseudo_random_function_f(generate_random_key(),2))
#print(c)
