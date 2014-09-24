import sys

try:
    if (len(sys.argv) <= 1) or \
       (sys.argv[2] not in ['+', '-', '*', '/', '%', '^']):
            print('usage: python3 ./solution.py', 'a_number',
                  '(an_operator +-*/%^)', 'a_number')
    else:
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
        elif z == '%':
            r = a % b

        print(r)

except:
    print('input error')
