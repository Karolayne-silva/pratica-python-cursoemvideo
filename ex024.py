import random
n = random.randint(0, 5)
num = int(input('Descubra o numero escolhido pelo computador de 0 a 5:'))
print('O número escolhido pelo computador foi: {}'.format(n))
if n == num:
    print('Você venceu! Parabéns')
else:
    print('Você perdeu!')
