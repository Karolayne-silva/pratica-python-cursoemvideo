vel = float(input('Digite a velocidade do seu carro: '))
if vel > 80:
    print('Você excedeu o limite, seu carro foi multado')
    multa = (vel-80)*7
    print('A multa foi de: R$ {:.1f}'.format(multa))
else:
    print('Dirigiu com segurança! Você não ultrapassou o limite estabelecido')
