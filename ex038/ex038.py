#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

while True:
    try:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    except:
        print('Entrada inválida, digite apenas números inteiros! Tente novamente...')
    else:
        break

if n1 > n2:
    print('O PRIMEIRO valor é o maior!')
elif n1 == n2:
    print('Os valores são IGUAIS!')
else:
    print('O Segundo valor é o maior!')
