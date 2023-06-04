# Demonstra a definição de uma função com um valor de retorno


def main():
    x = int(input("Qual o valor de x? "))
    print("x ao quadrado é", quadrado(x))


def quadrado(n):
    return n * n


main()
