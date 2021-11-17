#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze'
        'quinze', 'dezesseis', 'dezessete', 'dezoito'
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre zero e vinte: '))

    if num >=0 and num <=20:
        break
    else:
        print('Valor fora do intervalo, tente novamente!')

print(f'Você digitou o número {cont[num]}!')
