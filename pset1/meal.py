def main():
    tempo = input('Que horas são? ')
    hora = convert(tempo)
    if 7 <= hora <= 8:
        print('breakfast time')
    if 12 <= hora <= 13:
        print('lunch time')
    if 18 <= hora <= 19:
        print('dinner time')


def convert(tempos):
    horas, minutos = tempos.split(':')
    horas = float(horas)
    minutos = float(minutos)
    return (horas + (minutos / 60))


if __name__ == "__main__":
    main()
