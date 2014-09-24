import sys

if len(sys.argv) <= 1:
    print('usage: python3 ./solution.py', 'a_number', '(an_operator +-*/%^)',
          'a_number')

else:
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
