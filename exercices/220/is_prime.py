def is_prime(num):
    if (num == 1) | (num == 0):
        return False
    else:
        for i in range(2, int(pow(num, 0.5))+1):
            if num % i == 0:
                return False
        return True
