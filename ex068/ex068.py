#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*30)

opção = None
ganhou = None
contadorDeVitorias = 0
par_impar = None

while True:
    usuario = int(input('Diga um valor: '))
    while True:
        if usuario >= 0 and usuario <= 10:
            break
        else:
            print('Você deve digitar um valor entre 0 e 10!')

    computador = random.randint(0, 10)

    while opção is None or (opção not in 'PI'):
        opção = str(input('PAR OU ÍMPAR? [P/I]')).upper().strip()[0]

    print('-='*30)
    if (usuario + computador) % 2 == 0:
        par_impar = 'Par'
    else:
        par_impar = 'Ímpar'

    print(f'Você jogou {usuario} e o computador jogou {computador}. Total de {usuario+computador} \
é {par_impar}.')

    if opção in 'P':
        if (usuario + computador) % 2 == 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            contadorDeVitorias = contadorDeVitorias + 1
        else:
            print('Você PERDEU!')
            break
    elif  opção in 'I':
        if (usuario + computador) % 2 != 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            contadorDeVitorias = contadorDeVitorias + 1
        else:
            print('Você PERDEU!')
            break
    opção = None
    print('-='*30)

print(f'GAME OVER! Você venceu {contadorDeVitorias} vezes.')
