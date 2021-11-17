#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

lst = [0, 0, 0]
count = 0

for l in lst:
    while True:
        try:
            l = input(f'{count+1}º segmento:')
            lst[count] = float(l)
        except:
            print('Valor inválido, tente novamente...')
        else:
            count = count + 1
            break
print(lst)
lst.sort()

if(lst[0] + lst[1] > lst[2]):
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
