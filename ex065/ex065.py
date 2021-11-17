#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
#os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
#continuar a digitar valores.

maior = None
menor = None
sum = count = numero = 0
continua = 's'

#Enquanto resposta estiver em S maiúsculo ou s minúsculo:
while continua in 'Ss':
    while True:
        try:
            numero = int(input('Digite um número: '))
        except:
            print('Voce deve digitar um valor inteiro, tente novamente!')
        else:
            break

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < maior:
        menor = numero

    sum = sum + numero
    count = count + 1

    while True:
        continua = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]

        if continua != 'S' and continua != 'N':
            print('Opção inválida!')
        else:
            break

media = sum / count
print(f'Você digitou {count} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
