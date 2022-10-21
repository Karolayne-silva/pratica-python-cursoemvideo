produto = float(input('Insira o preço do produto: '))
pagamento = int(input('''Insira a forma de pagamento: 
1 - a vista dinheiro
2 - a vista cartão
3 - 2x cartão
4 - 3x ou mais cartão: '''))

if pagamento == 1:
    produtonovo = produto - (produto * 10/100)
    print('O valor a ser pago será R$ {:.1f}'.format(produtonovo))
elif pagamento == 2:
    produtonovo = produto - (produto * 5/100)
    print('O valor a ser pago será R$ {:.1f}'.format(produtonovo))
elif pagamento == 3:
    parcela_doisx = produto / 2
    print('O valor a ser pago será 2x de R$ {}'.format(parcela_doisx))
elif pagamento == 4:
    produtonovo = produto + (produto * 20 / 100)
    parcela = int(input('Digite quantas parcelas vão ser: '))
    valor = produtonovo / parcela
    print('Sua compra será parcelada em {}x de {:.1f} com juros'.format(parcela, valor))
    print('O valor a ser pago será {:.1f}'.format(produtonovo))
else:
    print('Opção inválida')

