#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

'''
Primeira forma de fazer:
num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
'''

#Segunda forma de fazer:
tupla = tuple()
i = 0
for i in range(4):
    n = int(input('Digite um número: '))
    tupla = tupla + (n,)

numerosPares = list()
for t in tupla:
    if t % 2 == 0:
        numerosPares.append(t)

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

try:
    posicaoNumeroTres = tupla.index(3)
except:
    posicaoNumeroTres = -1
if posicaoNumeroTres == -1:
    print('O valor 3 não apareceu nenhuma vez!')
else:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')

if len(numerosPares) > 0:
    print(f'Os valores pares digitados foram {numerosPares}')
else:
    print('Não foi digitado nenhum valor par!')
