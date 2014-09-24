import is_prime
r = []

for i in range(10000, 10050):
    if is_prime.is_prime(i):
        r.append(i)
print(str(r)[1:-1])
