# Demonstra a definição de uma função principal


def main():
    nome = input("Qual o seu nome? ")
    ola(nome)


def ola(para="mundo"):
    print("olá,", para)


main()
