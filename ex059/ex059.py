'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

def validaNumero(i):
    while True:
        try:
            if i == 0:
                numero = input('Digite a opção desejada: ')
            else:
                numero = input(f'{i}º valor: ')
            numero = int(numero)
        except:
            print('Valor inválido, tente novamente!')
        else:
            return numero


n1 = validaNumero(1)
n2 = validaNumero(2)
opção = None

while opção is None or (opção > 1 or opção < 5):
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')

    opção = validaNumero(0)
    print(f'OPCAO:   {opção}')

    if opção == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opção == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
    elif opção == 3:
        print(f'Entre {n1} e {n2} o maior é {max(n1, n2)}')
    elif opção == 4:
        n1 = validaNumero(1)
        n2 = validaNumero(2)
    elif opção == 5:
        break
    else:
        print('Opção Inválida!')
    print('=-'*20)
