#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
#(desconsiderando o flag)

numero = 0
count = 0
soma = 0

while numero != 999:
    while True:
        try:
            numero = int(input('Digite um número [999 pra parar]:'))
        except:
            print('Você deve digitar um número inteiro, tente novamente!')
        else:
            break
    #Refazer de modo que não precise verificar toda hora se o número digitado é 999
    if numero == 999:
        break
    else:
        count = count + 1
        soma = soma + numero

print(f'Você digitou {count} numeros e a soma entre eles foi {soma}.')
