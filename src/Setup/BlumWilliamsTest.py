# checks if n is blum integer

def blum_integer_test(n):

    if (n-3) % 4 == 0:
        return True
    else:
        return False
