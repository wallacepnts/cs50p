def main():
    dollars = dollars_to_float(input("Quanto foi a refeição? "))
    percent = percent_to_float(input("Quanto você quer de dar de gorjeta? "))
    # Converte em porcentagem
    tip = dollars * (percent / 100)
    print(f"Deixar ${tip:.2f}")


def dollars_to_float(d):
    # Remove o símbolo "$" e converte para número real
    d = float(d.replace('$', ''))
    return d


def percent_to_float(p):
    # Remove o símbolo "%" e converte para número inteiro
    p = int(p.replace('%', ''))
    return p


main()
