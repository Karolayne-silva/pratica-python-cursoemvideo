import math

angulo = float(input('Digite um angulo qualquer:'))
cos = math.cos(math.radians(angulo))
tang = math.atan(math.radians(angulo))
seno = math.sin(math.radians(angulo))

print('O angulo de {} tem cosseno no valor de {:.2f},\n tangente no valor de {:.2f}\n e seno no valor de {:.2f}'.format(angulo, cos, tang, seno))
