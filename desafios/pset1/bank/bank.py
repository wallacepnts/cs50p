ola = input('Saudação: ').strip().lower()

zero = ola.startswith("hello")
vinte = ola.startswith("h")

if zero:
    print('$0')
elif vinte:
    print('$20')
else:
    print('$100')
