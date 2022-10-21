distancia = float(input('Qual a distância da sua viagem em km:'))
if distancia <= 200:
    preco = distancia*0.50
    print('O preço da sua passagem vai ser: R$ {}'.format(preco))
else:
    preco = distancia*0.45
    print('O preço de sua passagem vai ser: R$ {}'.format(preco))

