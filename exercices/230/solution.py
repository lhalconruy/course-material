import is_prime
n = 100000000
i = False

while is_prime.is_prime(n) is not True:
    n = n + 1
print(n)
