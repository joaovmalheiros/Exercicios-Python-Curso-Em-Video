#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
#de uma Sequência de Fibonacci.

print('-'*80)
print('Sequência de Fibonacci')
print('-'*80)

while True:
    try:
        n = int(input('Quantos termos você quer mostrar? '))
    except:
        print('Digite um número inteiro!')
    else:
        break

i = 0
anterior = 0
aux = 0
atual = 0

print('~'*80)
while i < n:
    if i == 0 or i == 1:
        print(f'{atual} ->', end=' ')
        atual = 1
    else:
        aux = atual
        atual = atual + anterior
        anterior = aux
        print(f'{atual} ->', end=' ')
    i = i + 1
print('FIM')
print('~'*80)
