import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.pow(co, 2) + math.pow(ca, 2)
hipotenusa = math.sqrt(hipotenusa)

print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))
