#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
#progressão usando a estrutura while.

print('Gerador de P.A.')
print('-='*20)

while True:
    try:
        a = int(input('Primeiro termo: '))
        r = int(input('Razão da P.A.'))
    except:
        print('Entrada inválida, tente novamente!')
    else:
        break

n = 10

while n > 0:
    print(f'{a}', end=' -> ')
    a = a + r
    n = n - 1
print('FIM')
