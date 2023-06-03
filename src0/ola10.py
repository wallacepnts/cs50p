# Demonstra a definição de uma função com um parâmetro com um valor padrão


def ola(para="mundo"):
    print("olá,", para)


ola()
nome = input("Qual o seu nome? ")
ola(nome)
