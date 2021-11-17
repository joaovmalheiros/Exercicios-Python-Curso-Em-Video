#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

#Assistir à resolução para ver a outra forma de fazer:
for x in range(0, 11):
    print(10 - x)
    time.sleep(1)

print('BUM! BUM! POOW!')
