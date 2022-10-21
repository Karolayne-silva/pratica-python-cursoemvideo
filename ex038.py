from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
date = date.today().year
idade = date - ano

print('O atleta tem {} '.format(idade))

if idade <= 9:
    print('Você está na categoria MIRIN')
elif idade > 9 and idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Você está na categoria SÊNIOR')
else:
    print('Você está na categoria MASTER')
