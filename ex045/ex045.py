#Crie um programa que faça o computador jogar Jokenpô com você.



import random

print('Suas opcões:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogadasPossiveis = ['PEDRA', 'PAPEL', 'TESOURA']

while True:
    try:
        jogador = int(input('Qual é a sua jogada? '))
    except:
        print('Digite um valor entre 0 e 2!')
    else:
        break

print('JO\nKEN\nPO')

computador = random.randint(0, 2)

print('-='*20)
print(f'Computador jogou {jogadasPossiveis[computador]}')
print(f'Jogador jogou {jogadasPossiveis[jogador]}')
print('-='*20)

if jogador == 0:
    if computador == 0:
        print('EMPATE!')
    elif computador == 1:
        print('JOGADOR VENCEU!')
    elif computador == 2:
        print('COMPUTADOR VENCEU!')
elif jogador == 1:
    if computador == 0:
        print('JOGADOR VENCEU')
    elif computador == 1:
        print('EMPATE!')
    elif computador == 2:
        print('COMPUTADOR VENCEU!')
elif jogador == 2:
    if computador == 0:
        print('COMPUTADOR VENCEU!')
    elif computador == 1:
        print('JOGADOR VENCEU!')
    elif computador == 2:
        print('EMPATE!')
