#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ')
frase = frase.strip().upper()

palavras = frase.split()

junto = ''.join(palavras)
#junto = '*'join(palavras)  -->Junta as palavras com asteriscos ligando elas!

#There is no built-in function to reverse a String in Python.
#The fastest (and easiest?) way is to use a slice that steps backwards, -1.
#:: -> it goest through the entire String
#-1 -> it goes backwards
juntoReverso = junto[::-1]

'''
Outra forma de inverter a palavra:

juntoReverso = ''
#O for começa na última letra (é -1 porque se a string tem 10 letras, o último índice é 9)
#vai até a primeira (é 0, mas tem que sempre ir um a menos)
#o último parâmetro indica que o for vai voltando uma letra a cada loop
for letra in range(len(junto) - 1, -1, -1 ):
    juntoReverso = juntoReverso + junto[letra]

'''
print(f'O inverso de {frase} é {juntoReverso}')

if(junto == juntoReverso):
    print('É palíndromo!')
else:
    print('Não é palíndromo!')
