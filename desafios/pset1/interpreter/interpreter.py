expressao = input('Expressão: ')

x, y, z = expressao.split(" ")
x = float(x)
z = float(z)

if y == '+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
elif y == '/':
    print(x/z)
