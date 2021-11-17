#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
#termos dessa progressão.

print('-='*20)
print('10 Termos de uma P.A.')
print('-='*20)

while True:
    try:
        termo = int(input('Primeiro Termo: '))
        razao = int(input('Razão: '))
    except:
        print('Dados inválidos, tente novamente!')
    else:
        break

for i in range(1, 11):
    print(f'{termo}', end=' -> ')
    termo = termo + razao


'''
décimo = termo + (10-1) * razao
for i in range(termo, décimo + razão , razao):
    print(i, end=' -> ')
'''
print('Acabou!')
