peso = float(input('Digite seu peso kg: '))
altura = float(input('Digite sua altura m: '))
imc = peso/ (altura**2)

print('O IMC dessa linha é: {:.1f} '.format(imc))
print('Oxente que foi má não entendi má')

if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Você tem o peso ideal')
elif imc > 25 and imc <= 30:
    print('Você tem sobrepeso')
elif imc > 30 and imc <= 40:
    print('Você tem obesidade')
else:
    print('Você tem obesidade morbida')



