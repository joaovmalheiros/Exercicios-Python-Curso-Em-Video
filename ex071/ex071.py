#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
#ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
#valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*20, end='')
print('BANCO CEV', end='')
print('='*20)

cedulas = {'50':0, '20':0, '10':0, '1':0}

valor = int(input('Qual valor você quer sacar? R$'))

valorRestante = valor

if valorRestante > 50:
    cedulas['50'] = valorRestante // 50
    valorRestante = valorRestante - (50 * cedulas['50'])
if valorRestante > 20:
    cedulas['20'] = valorRestante // 20
    valorRestante = valorRestante - (20 * cedulas['20'])
if valorRestante > 10:
    cedulas['10'] = valorRestante // 10
    valorRestante = valorRestante - (10 * cedulas['10'])
if valorRestante > 1:
    cedulas['1'] = valorRestante // 1
    valorRestante = valorRestante - (20 * cedulas['20'])

for k,v in cedulas.items():
    print(f'Total de {v} cédulas de R${k}')

print('Volte sempre ao banco CEV! Tenha um bom dia!')
