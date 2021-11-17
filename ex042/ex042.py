'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

lst = [0, 0, 0]
posicao = 0

for l in lst:
    while True:
        try:
            l = float(input(f'{posicao+1}º segmento: '))
        except:
            print('Valor inválido, tente novamente!')
        else:
            lst[posicao] = l
            posicao = posicao + 1
            break

lst.sort()
print(lst)

if (lst[0] + lst[1]) > lst[2]:
    #Também pode ser lst[0] == lst[1] == lst[2]
    if(lst[0] == lst[1] and lst[1] == lst[2]):
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    #Também pode ser lst[0] != lst[1] != lst[2] != lst[1]
    elif(lst[0] != lst[1] and lst[1] != lst[2]):
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
    #Se pode formar um triângulo e não é equilátero, nem escaleno, é porque é isósceles:
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
