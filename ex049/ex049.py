# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
#um laço for.

while True:
    try:
        numero = int(input('Digite um número para ver a tabuada: '))
    except:
        print('Digite um número válido!')
    else:
        break

for x in range(1, 11):
    print(f'{x} * {numero} = {x*numero}')
