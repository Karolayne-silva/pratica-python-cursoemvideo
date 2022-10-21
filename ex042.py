import random
from time import sleep
print('---- Vamos jogar Pedra, Papel e Tesoura ----\n')
j1 = str(input('Escolha pedra, papel, tesoura: ')).upper()

lista = ['PEDRA', 'PAPEL', 'TESOURA']
j2 = random.choice(lista)


if j1 == 'PEDRA' or j1 == 'PAPEL' or j1 == 'TESOURA':
    print('Pedra')
    sleep(1)
    print('Papel')
    sleep(1)
    print('e TESOUU')
    sleep(0.5)
    print('RA')

    print('*' * 20)
    print('Você escolheu: {} e o computador escolheu: {}'.format(j1, j2))
    print('*' * 20)

    if j1 == j2:
        print('\033[0;32;40m EMPATOU!!!')

    elif j1 == 'TESOURA' and j2 == 'PAPEL':
        print('\033[0;32;40m VOCÊ GANHOU!')

    elif j1 == 'TESOURA' and j2 == 'PEDRA':
        print('\033[0;32;40m COMPUTADOR GANHOU!')

    elif j1 == 'PAPEL' and j2 == 'PEDRA':
        print('\033[0;32;40m VOCÊ GANHOU!')

    elif j1 == 'PAPEL' and j2 == 'TESOURA':
        print('\033[0;32;40m COMPUTADOR GANHOU!')

    elif j1 == 'PEDRA' and j2 == 'TESOURA':
        print('\033[0;32;40m VOCÊ GANHOU!')

    elif j1 == 'PEDRA' and j2 == 'PAPEL':
        print('\033[0;32;40m COMPUTADOR GANHOU!')
else:
    print('Palavra inválida!')





