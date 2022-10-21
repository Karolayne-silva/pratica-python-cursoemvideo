salario = float(input('Digite o valor do seu salário: '))
casa = float(input('Digite o valor da casa: '))
ano = int(input('Digite em quantos anos deseja pagar: '))
meses = 12 * ano
prestacao = casa / meses
excede = salario * 30/100

if prestacao > excede:
    print('Seu emprestimo foi negado!')
else:
    print('Seu emprestimo foi concedido!')
