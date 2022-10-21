dias = int(input('Por quantos dias o carro foi alugado: '))
km = int(input('Quantos km o carro percorreu: '))
dias = dias*60
km = 0.15*km
preco = dias + km

print('O total a pagar é R${:.2f}'.format(preco))
