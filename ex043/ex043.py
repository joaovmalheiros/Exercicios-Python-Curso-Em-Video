'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

while True:
    try:
        peso = float(input('Qual é o seu peso? (kg) '))
        altura = float(input('Qual é a sua altura? (m) '))
    except:
        print('Dados inválidos, tente novamente!')
    else:
        break

imc = peso / (altura * altura)

print(f'O imc dessa pessoa é {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso normal!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc < 40:
    print('Você está com obesidade, cuidado!')
else:
    print('Você está com obesidade mórbida, cuidado!')
