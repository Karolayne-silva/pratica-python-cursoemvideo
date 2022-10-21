salario = float(input('Informe seu salário: '))
if salario > 1250.00:
    aumento = salario*10/100
    novo = salario + aumento
else:
    aumento = salario*15/100
    novo = salario + aumento
print('Seu salário é {} e você teve um aumento de {:.2f} seu novo salário é {}'.format(salario, aumento, novo))
