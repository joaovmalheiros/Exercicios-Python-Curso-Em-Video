#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

while True:
    try:
        svalue = input('Digite um número: ')
        ivalue = int(svalue)
    except:
        print('Dado inválido!')
    else:
        break

print(f'Dobro de {ivalue} = {ivalue*2}')
print(f'Triplo de {ivalue} = {ivalue*3}')
print(f'Raiz quadrada de {ivalue} = {math.sqrt(ivalue):.2f}')
