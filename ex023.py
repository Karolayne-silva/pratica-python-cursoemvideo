nome = str(input('Digite seu nome completo: ')).strip()
separacao = nome.split()
primeiro = separacao[0]
ultimo = separacao[-1]
print('primeiro nome: {}'.format(primeiro))
print('ultimo nome: {}'.format(ultimo))
