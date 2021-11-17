# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
#encerrará quando ele disser que quer mostrar 0 termos.

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
count = 0

while n > 0:
    print(f'{a}', end=' -> ')
    a = a + r
    n = n - 1
    count = count + 1
    if n == 0:
        print('PAUSA')
        while True:
            try:
                n = int(input('Quantos termos você quer mostrar a mais? '))
            except:
                print('Entrada inválida, tente novamente!')
            else:
                break
print(f'Progressão finalizada com {count} termos mostrados.')
