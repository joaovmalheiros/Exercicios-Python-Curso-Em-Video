# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
#elas (desconsiderando o flag).

sum = count = 0
opção = None

while True:
    while True:
        try:
            opção = int(input('Digite um valor (999 para parar): '))
        except:
            print('Digite apenas valores inteiros!')
        else:
            break

    if opção == 999:
        break
    else:
        sum = sum + opção
        count = count + 1

print(f'A soma dos {count} valores foi {sum}!')
