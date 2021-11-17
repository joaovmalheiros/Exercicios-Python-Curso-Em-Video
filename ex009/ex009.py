#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

aux = True
while aux == True:
    svalue = input('Digite um numero inteiro:')
    try:
        ivalue = int(svalue)
        aux = False
    except:
        print('Valor inválido!')

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for t in tabuada:
    print(f'{ivalue} * {t} = {ivalue * t}')
