#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

from math import sqrt
from math import hypot

while True:
    try:
        catOposto = input('Comprimento do cateto oposto: ')
        catAdjacente = input('Comprimento do cateto adjacente: ')
        catOposto = float(catOposto)
        catAdjacente = float(catAdjacente)
    except:
        print('Dados inválidos, tente novamente...')
    else:
        break

#hipotenusa = sqrt(((catOposto)**2) + ((catAdjacente)**2)) #Utilizando conceito matemático
hipotenusa = hypot(catOposto, catAdjacente) #Utilizando função do módulo math

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
