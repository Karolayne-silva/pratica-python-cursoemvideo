nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2

print('Sua média foi {}'.format(media))
if media < 5.0:
    print('Aluno Reprovado!')
elif media == 5.0 or media <= 6.9:
    print('Aluno em Recuperação!')
elif media >= 7.0:
    print('Aluno Aprovado')
