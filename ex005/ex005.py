#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

while True:
    try:
        svalue = input('Digite um numero:')
        ivalue = int(svalue)
    except:
        print('Valor inválido!')
    else:
        break

print(f'Analisando o valor {ivalue}, seu antecessor é o {ivalue-1} e o sucessor é {ivalue+1}')
