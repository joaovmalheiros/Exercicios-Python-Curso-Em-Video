#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
#qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

while True:
    try:
        valorInteiro = int(input('Digite um número inteiro: '))
    except:
        print('Valor inválido, tente outra vez!')
    else:
        break

while True:
    try:
        escolha = int(input('Escolha uma das bases para conversão:\n\
[1] converter para BINÁRIO\n\
[2] converter para OCTAL\n\
[3] converter para HEXADECIMAL\n\
Sua opção: '))
        if escolha < 1 or escolha > 3:
            print('Você deve escolher uma opção entre 1 e 3!')
            continue
    except:
        print('Você deve digitar um valor inteiro entre 1 e 3!')
    else:
        break

#Utilizar fatiamento de strings para tirar os caracteres iniciais que indicam de qual base é o valor:
if escolha == 1:
    print(f'{valorInteiro} convertido para BINÁRIO é igual a {bin(valorInteiro)[2:]}!')
elif escolha == 2:
    print(f'{valorInteiro} convertido para OCTAL é igual a {oct(valorInteiro)[2:]}!')
elif escolha == 3:
    print(f'{valorInteiro} convertido para HEXADECIMAL é igual a {hex(valorInteiro)[2:]}!')
