#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

soma = 0
count = 0

for x in range(1, 7):
    while True:
        try:
            x = int(input('Digite um número: '))
        except:
            print('Valor inválido, tente novamente!')
        else:
            break
    if x % 2 == 0:
        count = count + 1
        soma = soma + x

print(f'Você informou {count} números pares e a soma deles é {soma}')
