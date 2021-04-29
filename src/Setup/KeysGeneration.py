def public_key(n, u, h, c, k, L):
    pub_key = str(n) + str(u) + str(h) + str(c) + str(int.from_bytes(k, 'little')) + str(L)

    return pub_key

def secret_key(n):
    n_factorization = ""
    for i in range(1, n + 1):
        if n % i == 0:
            n_factorization += str(i)
    sec_key = n_factorization

    return sec_key
