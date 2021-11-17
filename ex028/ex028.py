#Escreva um programa que faça o computador "pensar" em um número inteiro entre
#0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
#computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep #pesquisar mais sobre essa biblioteca

valorAleatorio = random.randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

while True:
    guess = input('Em que número eu pensei?')
    try:
        guess = int(guess)
    except:
        print('Digite uma entra numérica entre 0 e 5!')
        continue
    if(guess >= 0 and guess <= 5):
        break
    else:
        print('O número digitado está fora do intervalo solicitado, tente novamente!')

print('PROCESSANDO...')
sleep(3) #Espera 3 segundos
if guess != valorAleatorio:
    print(f'GANHEI! Eu pensei no número {valorAleatorio} e não no {guess}')
else:
    print('PARABÉNS! Você conseguiu me vencer!')

#Pesquisar como coloca cor no python
