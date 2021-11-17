#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

sValue = None

while ((sValue == None) or ((iValue < 0) or (iValue > 9999))):
    try:
        sValue = input('Digite um numero de 0 a 9999: ')
        iValue = int(sValue)
    except:
        print('Valor inválido, tente novamente...')
        iValue = -1

casas = ['Milhar', 'Centena', 'Dezena', 'Unidade']
print(f'Analisando o número {iValue}')

for x in range(len(sValue)):
    print(f'{casas[x]}: {sValue[x]}')

#Converter valor para int e fazer com módulo de divisão
