r1 = float(input('Digite o tamanho da reta: '))
r2 = float(input('Digite o tamanho da reta: '))
r3 = float(input('Digite o tamanho da reta: '))

if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('As retas podem formar um triângulo')
    if r1 == r2 and r2 == r3 and r1 == r3:
        print('Esse é um triângulo equilatero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Esse é um triângulo escaleno')
    else:
        print('Esse é um triângulo isosceles')
else:
    print('As retas NÃO podem formar um triângulo')
