num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    maior = num1
    print('O primeiro valor {} é o maior'.format(maior))
elif num2 > num1:
    maior = num2
    print('O segundo valor {} é o maior'.format(maior))
elif num1 == num2:
    print('Não há valor maior, os dois valores são iguais')
