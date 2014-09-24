import is_prime
r = 0

for i in range(1000):
    if is_prime.is_prime(i):
        r = r + i
print(r)
