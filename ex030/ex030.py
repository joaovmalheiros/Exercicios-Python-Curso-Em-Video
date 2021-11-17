#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

while True:
    num = input('Digite um número inteiro: ')
    try:
        num = int(num)
    except:
        print('Valor inválido, tente novamente!')
    else:
        break

if(num % 2 == 0):
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')
