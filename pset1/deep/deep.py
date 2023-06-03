quarenta_e_dois = input('Qual a questão fundamental da vida, '
                        'o universo e tudo mais? ').strip().lower()

match quarenta_e_dois:
    case '42' | 'forty two' | 'forty-two':
        print('Yes')
    case _:
        print('No')
