n = int(input('Digite um valor: '))
print('A tabuada de {} é: '.format(n))
contador = 0
print('-' * 12)
while contador < 11:
    print('{}x{} = {}'.format(n, contador, n*contador))
    contador = contador + 1
print('-' * 12)
