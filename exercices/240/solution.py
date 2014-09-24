f = [1, 2, 3]

for i in range(7):
    f.append(f[i+1] + f[i+2])

print(str(f)[1:-1] + ".")
