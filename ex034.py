num = int(input('Digite um número: '))
conversao = int(input('''Escolha um numero de 1 a 3:
1- binario
2- octal
3- hexadecimal: '''))

if conversao == 1:
    print('Seu número em binário {}'.format(bin(num)[2:]))
elif conversao == 2:
    print('Seu número em octal {}'.format(oct(num)[2:]))
elif conversao == 3:
    print('Seu número em Hexadecimal {}'.format(hex(num)[2:]))
else:
    print('Número não aceito')

