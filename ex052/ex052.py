#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Colocar cores no código!

while True:
    try:
        numero = int(input('Digite um número inteiro: '))
    except:
        print('Valor inválido, tente novamente!')
    else:
        break

count = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        count = count + 1

print(f'O número {numero} foi divisível {count} vezes')

if count == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele não é primo!')
