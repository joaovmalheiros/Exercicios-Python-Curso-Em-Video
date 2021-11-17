#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
#de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

lista = list()

#Dá para fazer sem utilizar a lista e o loop:
# n = (randint(1,10), randint(1,10), randint(1,10)...)
i = 0
while i != 5:
    valorAleatorio = randint(1, 10)
    lista.append(valorAleatorio)
    i = i + 1

print('Os valores sorteados foram: ', end='')
tupla = tuple(sorted(lista))
print(tupla)
print(f'O maior valor sorteado foi {max(tupla)} e o menor valor sorteado foi {min(tupla)}')
