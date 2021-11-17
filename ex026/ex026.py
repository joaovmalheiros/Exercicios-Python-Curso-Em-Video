#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')
frase= frase.strip()
frase = frase.lower()

count = 0

primeiraPosicao = frase.find('a')
ultimaPosicao = frase.rfind('a')

for letter in frase:
    if letter.lower() == 'a':
        count = count + 1

print(f'A letra A aparece {count} vezes na frase.')
print(f'A primeira letra A apareceu na posicao {primeiraPosicao + 1}')
print(f'A última letra A apareceu na posicao {ultimaPosicao + 1}')
