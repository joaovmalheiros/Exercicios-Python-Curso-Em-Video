#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
#vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep #pesquisar mais sobre essa biblioteca

def verificaPalpite():
    while True:
        try:
            palpite = input('Qual é o seu palpite? ')
            palpite = int(palpite)
        except:
            print('Valor inválido! Tente novamente!')
        else:
            return palpite

computador = random.randint(0, 10)
tentativas = 0
acertou = False

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

while not acertou:
    palpite = verificaPalpite()
    tentativas = tentativas + 1
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
    elif palpite < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print(f'Acertou com {tentativas} tentativas! Parabéns!')
        break
