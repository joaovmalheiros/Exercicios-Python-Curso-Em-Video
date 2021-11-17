#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

opção = None

while True:
    while True:
        try:
            opção = int(input('Quer ver a tabuada de qual valor? '))
        except:
            print('Digite um valor inteiro!')
        else:
            break

    print('-'*20)

    if opção < 0:
        print('PROGRAMA TABUADA encerrado, volte sempre!')
        break
    else:
        for t in tabuada:
            #fazer assim ou utilizando for com range!
            print(f'{opção} x {t} = {opção * t}')

    print('-'*20)
