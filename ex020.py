nome = str(input('Digite o nome de uma cidade:')).strip()
divisao = nome.split()
print('SANTO' in divisao[0].upper())

#outra forma:
#print(nome[:5].upper == 'SANTO')
