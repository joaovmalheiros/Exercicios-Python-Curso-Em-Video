#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

while True:
    try:
        angulo = input('Digite o ângulo que você deseja (em graus): ')
        angulo = float(angulo)
    except:
        print('Valor inválido, tente novamente...')
    else:
        break

anguloRad = math.radians(angulo)
seno = math.sin(anguloRad)
cosseno = math.cos(anguloRad)
tangente = math.tan(anguloRad)

print(f'O angulo de {angulo:.2f} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo:.2f} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo:.2f} tem a TANGENTE de {tangente:.2f}')
