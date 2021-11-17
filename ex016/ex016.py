#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

while True:
    try:
        sValue = input('Digite um valor: ')
        fValue = float(sValue)
    except:
        print('Dado inválido, tente novamente...')
    else:
        break

print(f'O valor digitado foi {fValue} e  sua porção inteira é {trunc(fValue)}')

'''
if '.' not in sValue:
    print(f'Parte inteira: {int(fValue)}')
else:
    valorDivido =  sValue.split('.')
    parteInteira = int(valorDivido[0])
    parteDecimal = float('0.' + valorDivido[1])
    print(f'Parte inteira: {parteInteira}', type(parteInteira))
    print(f'Parte decimal: {parteDecimal}', type(parteDecimal))
'''
