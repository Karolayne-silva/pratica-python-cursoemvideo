from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
date = date.today().year
idade = date - ano
alistar = idade - 18

print('Quem nasceu em {} tem {} em {}'.format(ano, idade, date))

if idade == 18:
    print('\nJá é hora de se alistar ao serviço militar')
elif idade > 18:
    print('\nVocê já passou do tempo de se alistar ao serviço militar')
    print('Passou {} anos do prazo de se alistar'.format(alistar))
elif idade < 18:
    print('\nVocê ainda vai se alistar ao serviço militar!')
    print('Faltam {} ano(s) para você se alistar'.format(abs(alistar)))
