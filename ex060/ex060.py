#Faça um programa que leia um número qualquer e mostre o seu fatorial

while True:
    try:
        numero = int(input('Digite um número inteiro para calcular seu fatorial: '))
    except:
        print('Você deve digitar um número inteiro, tente novamente!')
    else:
        break

fat = 1

print(f'Calculando {numero}! = ', end=' ')

if numero != 1 and numero != 0:
    #Se conhecer os limites, dá pra usar o for (só usa while se não tiver os limites!):
    for i in range(numero, 0, -1):
        fat = fat * i
        print(f'{i} x ' if  i > 1 else f'{i} = ', end='')
print(f'= {fat}')
