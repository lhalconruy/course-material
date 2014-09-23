import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    z = sys.argv[2]

    if z == '+':
        r = a + b
    elif z == '-':
        r = a - b
    elif z == '*':
        r = a * b
    elif z == '/':
        r = a / b

    print(r)

except:
    print('input error')
